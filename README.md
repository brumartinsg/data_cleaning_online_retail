# Português-BR: 📊 Online Retail — Projeto de Limpeza de Dados

**Autora:** Bruna Martins  
**Cargo:** Data Analyst  

---

## 📌 Objetivo do Projeto

Realizar a limpeza e padronização de um dataset de varejo do mundo real, preparando-o para:

- Análises em Business Intelligence  
- Engenharia de features  
- Normalização de preços (preço por grama)  
- Análises agregadas por marca  
- Aplicações futuras em modelagem de dados  

---

## 🧹 Pipeline de Limpeza

### 1️⃣ Tratamento de Datas
- Conversão da coluna `OrderDate` para formato datetime  
- Criação das variáveis derivadas `Year` e `Month`  

### 2️⃣ Tratamento de Preço Unitário
- Remoção de produtos sem preço válido  

---

# 📊 Online Retail — Data Cleaning Project

**Author:** Bruna Martins  
**Role:** Data Analyst  

---

## 📌 Project Objective

Clean and standardize a real-world retail dataset to prepare it for:

- Business Intelligence analysis
- Feature engineering
- Price normalization (price per gram)
- Brand-level aggregation
- Future modeling tasks

---

## 🧹 Cleaning Pipeline

### 1️⃣ Date Treatment
- Converted `OrderDate` to datetime
- Created `Year` and `Month` features

### 2️⃣ Unit Price Treatment
- Removed products without valid prices
- Imputed missing prices using product-level median
- Removed residual null values

### 3️⃣ Weight Treatment
- Extracted numeric weight values from raw text
- Extracted weight units
- Normalized units (g, kg, mg, oz, lb)
- Converted all mass units to grams
- Standardized mass units to `"g"`

### 4️⃣ Text Standardization
- Cleaned `ProductName`
- Cleaned `Brand`
- Removed special characters
- Lowercased text
- Standardized spacing

---------

## 🗂 Project Structure

