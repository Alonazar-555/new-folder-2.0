# Dash + Plotly Demo Dashboard

דוגמה קצרה ל־Dashboard ב־Python באמצעות **Dash** ו־**Plotly Express**.  
האפליקציה מציגה גרף עמודות פשוט המבוסס על `pandas.DataFrame`.

---

## תכולת הפרויקט

- `dashboard.py` — אפליקציית Dash שמריצה שרת מקומי ומציגה גרף.
- `test.py` — קובץ בדיקה/דוגמה בסיסי.

---

## דרישות

- Python 3.9+ (מומלץ)

ספריות:
- `dash`
- `plotly`
- `pandas`

---

## התקנה (Windows / macOS / Linux)

### יצירת סביבת עבודה (מומלץ)

```bash
python -m venv .venv
```

הפעלה:

```bash
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

### התקנת תלויות

```bash
pip install dash plotly pandas
```

---

## הרצה

```bash
python dashboard.py
```

לאחר ההרצה, פתח/י בדפדפן את הכתובת שמודפסת בטרמינל (בדרך כלל):
- `http://127.0.0.1:8050/`

---

## מה תרא/י?

- כותרת: **Sample Dashboard**
- תיאור קצר
- גרף עמודות (Bar Chart) עם קטגוריות A–D וערכים לדוגמה

---

## התאמה אישית מהירה

אפשר לערוך את הדאטה והגרף בתוך `dashboard.py`:
- לשנות את ה־DataFrame (`df`)
- להחליף סוג גרף (למשל `px.line`, `px.scatter`)
- לעדכן Layout (כותרות/רכיבי Dash)

---

## תקלות נפוצות

- **Port תפוס (8050)**: סגור/י תהליך אחר או שנה/י פורט:

```python
app.run_server(debug=True, port=8051)
```

- **בעיה בהרצת Activate.ps1 ב־PowerShell**: ייתכן שתצטרך/י לאפשר הרצת סקריפטים (Execution Policy) או להריץ דרך `cmd`.

---

## רישיון

בחר/י רישיון לפי הצורך (למשל MIT). כרגע לא הוגדר רישיון בפרויקט.

