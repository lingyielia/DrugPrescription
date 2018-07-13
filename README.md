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
│   └── README.md
├── insight_testsuite
│   ├── run_tests.sh
│   └── tests
│       └── test_1
│           ├── README.md
│           ├── input
│           │   └── itcont.txt
│           └── output
│               └── top_cost_drug.txt
├── output
│   └── README.md
├── run.sh
└── src
    ├── README.md
    ├── de_cc_data.txt
    ├── itcont.txt
    ├── pharmacyCount_large.ipynb
    ├── pharmacyCount_smallsize.ipynb
    └── result.txt
```
