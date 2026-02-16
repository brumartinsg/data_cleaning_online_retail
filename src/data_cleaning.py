"""
Online Retail - Data Cleaning Pipeline
Author: Bruna Martins
Role: Data Analyst

Objective:
Clean and standardize a real-world retail dataset to prepare it
for analysis and feature engineering.
"""

import pandas as pd
import numpy as np
import re


# =========================
# 1. LOAD DATA
# =========================

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path, sep=",", decimal=".")


# =========================
# 2. DATE TREATMENT
# =========================

def clean_order_date(df: pd.DataFrame) -> pd.DataFrame:
    df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
    df["Year"] = df["OrderDate"].dt.year
    df["Month"] = df["OrderDate"].dt.month
    return df


# =========================
# 3. UNIT PRICE TREATMENT
# =========================

def clean_unit_price(df: pd.DataFrame) -> pd.DataFrame:
    
    # Remove products with no valid price
    valid_price_count = df.groupby("ProductName")["UnitPrice"].count()
    products_no_valid_price = valid_price_count[valid_price_count == 0].index.tolist()
    df = df[~df["ProductName"].isin(products_no_valid_price)]

    # Impute missing prices with product median
    df["UnitPrice"] = df.groupby("ProductName")["UnitPrice"].transform(
        lambda x: x.fillna(x.median())
    )

    # Remove residual nulls
    df = df.dropna(subset=["UnitPrice"])

    return df


# =========================
# 4. WEIGHT TREATMENT
# =========================

def split_weight(value):
    if pd.isnull(value):
        return np.nan, np.nan

    value = str(value).strip()

    number_match = re.search(r"\d+[\.,]?\d*", value)
    number = float(number_match.group().replace(",", ".")) if number_match else np.nan

    unit_part = re.sub(r"\d+[\.,]?\d*", "", value).strip()
    unit = unit_part if unit_part != "" else np.nan

    return number, unit


def normalize_unit(value):
    if pd.isnull(value):
        return np.nan

    value = str(value).lower()

    if re.search(r"\b(g|gr|grs|gr\.|gram|grams|gramos|gm|grame)\b", value):
        return "g"

    if re.search(r"\bkg\b", value):
        return "kg"

    if re.search(r"\bmg\b", value):
        return "mg"

    if re.search(r"\bml\b", value):
        return "ml"

    if re.search(r"\bl\b", value):
        return "l"

    if re.search(r"\boz\b", value):
        return "oz"

    if re.search(r"\blb\b", value):
        return "lb"

    return value.strip()


def convert_to_grams(row):
    value = row["Weight_value"]
    unit = row["Weight_unit_clean"]

    if pd.isnull(value) or pd.isnull(unit):
        return value

    if unit == "g":
        return value
    elif unit == "kg":
        return value * 1000
    elif unit == "mg":
        return value / 1000
    elif unit == "oz":
        return value * 28.3495
    elif unit == "lb":
        return value * 453.592
    else:
        return value


def clean_weight(df: pd.DataFrame) -> pd.DataFrame:

    df[["Weight_value", "Weight_unit"]] = (
        df["Raw_Weight"]
        .apply(lambda x: pd.Series(split_weight(x)))
    )

    df["Weight_unit_clean"] = df["Weight_unit"].apply(normalize_unit)

    df["Weight_value"] = df.apply(convert_to_grams, axis=1)

    mass_units = ["g", "kg", "mg", "oz", "lb"]
    df.loc[df["Weight_unit_clean"].isin(mass_units), "Weight_unit_clean"] = "g"

    return df


# =========================
# 5. TEXT STANDARDIZATION
# =========================

def clean_text(text):
    if pd.isnull(text):
        return np.nan

    text = str(text).strip().lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s]", "", text)

    return text


def clean_text_fields(df: pd.DataFrame) -> pd.DataFrame:
    df["ProductName_clean"] = df["ProductName"].apply(clean_text)
    df["Brand_clean"] = df["Brand"].apply(clean_text)
    return df


# =========================
# MAIN PIPELINE
# =========================

def main():

    df = load_data("data/raw/online_retail_real_world.csv")

    df = clean_order_date(df)
    df = clean_unit_price(df)
    df = clean_weight(df)
    df = clean_text_fields(df)

    df.to_csv("data/processed/online_retail_cleaned.csv", index=False)


if __name__ == "__main__":
    main()
