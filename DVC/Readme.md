
1. Create virtual environment: `create env -n dvc`
2. install dvc: `pip install dvc`
3. `git init` and `python -m dvc init`
4. Add data `python -m dvc add Salary_Data.csv`
5. `git add Salary_Data.csv.dvc .gitignore`
6. `git commit -m "Track Dataset version 1 with DVC"`
7. Alterdata(or you can run `alterdata.py`)
8. `git checkout`

9. How to bring previous version?
`python -m dvc pull --force` 
from above command data will be reverted to previous version
We can also do above process for `.pkl` ML models.
