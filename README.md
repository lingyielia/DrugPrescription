# Pharmacy Counting
__Notice__  
I used `Python3` in this task.  
In the script, I used `import sys`

## How to start
In the shell, locate my repo's root directory, run:
```shell
bash run.sh
```

## How I approach this task
1. I first open 2 dictionaries. One records drug name and its total cost. The other records drug name and its unique prescribers.
2. I then combine these 2 dictionaries' information into a list of tuples. Each tuple contains drug name, count of unique prescribers, total cost.
3. After sorting the list of tuples by total cost in descending order, store the final result to output file.

## How to save memory when computing
- Read file one line each time and process it before read the next line.
- Convert string to float or integer when possible, as string takes more space.
- Do in-place sorting.

## Repo directory structure
The directory structure for this repo:

```shell
.
├── README.md
├── input
│   └── itcont.txt
├── insight_testsuite
│   ├── run_tests.sh
│   └── tests
│       ├── test_1
│       │   ├── input
│       │   │   └── itcont.txt
│       │   └── output
│       │       └── top_cost_drug.txt
│       ├── test_2
│       │   ├── input
│       │   │   └── itcont.txt
│       │   └── output
│       │       └── top_cost_drug.txt
│       ├── test_3
│       │   ├── input
│       │   │   └── itcont.txt
│       │   └── output
│       │       └── top_cost_drug.txt
│       ├── test_4
│       │   ├── input
│       │   │   └── itcont.txt
│       │   └── output
│       │       └── top_cost_drug.txt
│       └── test_5
│           ├── input
│           │   └── itcont.txt
│           └── output
│               └── top_cost_drug.txt
├── output
│   └── top_cost_drug.txt
├── run.sh
└── src
    └── drug_usage.py
```

## Test cases
- test_1: Originally provided.
- test_2: Contains 2 rows with the same prescriber and drug name.
- test_3: Contains integer and float in the drug_cost column.
- test_4: empty input file.
- test_5: Contains missing value in one row.
