import pandas as pd
import math

# Read in the data
schools = pd.read_csv("Data/schools.csv")

# Preview the data
schools.head()

school_test = schools.copy()
school_test["total_SAT"]=school_test["average_math"]+school_test["average_reading"]+school_test["average_writing"]
top_10_schools = school_test.loc[:,["school_name","total_SAT"]]
top_10_schools = top_10_schools.sort_values(["total_SAT"],ascending = False)
top_10_schools.index=range(0,len(top_10_schools))
top_10_schools = top_10_schools.loc[0:9,:]
print(top_10_schools)

school_test2 = school_test.copy()
boroughs = school_test2.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)
largest_std_dev = school_test2[["borough"]]
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})
largest_std_dev.reset_index(inplace=True)


print(largest_std_dev)

bestschools1 = schools[(schools["average_math"] >= 640)]
best_math_schools = bestschools1.loc[:,["school_name","average_math"]]
best_math_schools = best_math_schools.sort_values(["average_math"],ascending = False)
    
print(best_math_schools)