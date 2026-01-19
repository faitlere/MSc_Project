import os
from pathlib import Path
import pandas as pd
import pyreadstat
import glob

data_dir = Path("/Users/faitholalere/Documents/Masters/Dissertation/Data/BPHS&UKHLS indresp files")
os.chdir(data_dir)

#output path
out_path = Path("/Users/faitholalere/Documents/Masters/Dissertation/Data/Combined Data/combined_core_analysis.csv")

# core variables
Core_variables = [
    "sex", "age_dv", "mstat", "nchild_dv", "rach16_dv",
    "jbstat", "jbhrs", "jbmngr", "jbsize", "jbsoc00_cc",
    "paygu_dv", "paynu_dv",
    "hiqual_dv"
]


# read sav files not tab
sav_files = sorted(glob.glob("*.sav"))
print(f"Found {len(sav_files)} .sav files to process.")

year_map = {
    # BHPS waves (ba, bb, ..., br)
    "ba": 1991, "bb": 1992, "bc": 1993, "bd": 1994, "be": 1995,
    "bf": 1996, "bg": 1997, "bh": 1998, "bi": 1999, "bj": 2000,
    "bk": 2001, "bl": 2002, "bm": 2003, "bn": 2004, "bo": 2005,
    "bp": 2006, "bq": 2007, "br": 2008,
    # UKHLS waves (a, b, ..., n)
    "a": 2009, "b": 2010, "c": 2011, "d": 2012, "e": 2013,
    "f": 2014, "g": 2015, "h": 2016, "i": 2017, "j": 2018,
    "k": 2019, "l": 2020, "m": 2021, "n": 2023
}

first_file = True
#process files
for fname in sav_files:
    print(f"Processing {fname}...")
    try:
        df, meta = pyreadstat.read_sav(fname, apply_value_formats=True, formats_as_category=False)
        wave_prefix = Path(fname).stem.split("_")[0] # identify wave
        cols_to_keep = ["pidp"] # this is the unique idnetifier
        rename_map = {}

        for stem in Core_variables:
            col_name = f"{wave_prefix}_{stem}"
            if col_name in df.columns:
                cols_to_keep.append(col_name)
                rename_map[col_name] = stem
            elif stem in df.columns:
                cols_to_keep.append(stem)

        df_small = df[cols_to_keep].copy()

        df_small['wave'] = wave_prefix
        df_small['year'] = year_map.get(wave_prefix, pd.NA)
        df_small['source_file'] = fname
        df_small.rename(columns=rename_map, inplace=True)
# reorder cols
        final_col_order = ["pidp", "wave", "year", "source_file"] + [c for c in df_small.columns if
                                                                     c not in ["pidp", "wave", "year", "source_file"]]
        df_small = df_small[final_col_order]

#make into csv
        df_small.to_csv(
            out_path,
            mode='a',
            header=first_file,
            index=False
        )

        first_file = False
        del df, df_small, meta # this helps with memory

    except Exception as e:
        print(f"  -> ERROR  {fname}: {e}")
        continue
print(f"\nDone - file saved to: {out_path}")
