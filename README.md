# USAGE INSTRUCTIONS

## Step 1: Getting bank transactions
Download bank transactions, save them to a folder (I recommend a specific YNAB folder, examples will use ynab/conversion folder)

## Step 2: Converting the file
1. Open your terminal of choice (Windows: `cmd.exe`, `powershell`), this will usually open in your personal folder (eg. /User/rhea)
2. Change directory to your ynab folder `cd ynab`
3. Use python to convert the file:
    * `python.exe ing2ynab.py <path_to_sourcefile>.csv <path_to_target_filename>.csv`
    * full example: `python.exe
    ing2ynab.py .\conversion\NL87INGB0009396396_01-11-2018_18-11-2018.csv .\conversion\ing20181101.csv`

## Step 3: Uploading the file to YNAB
Open YNAB in your browser and drag the `.csv` file anywhere in the app. This will upload the file. You might need to set the dates, but YNAB will prompt for that.
