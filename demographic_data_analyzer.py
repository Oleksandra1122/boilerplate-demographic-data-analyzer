import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = (df[df['sex']=='Male']['age'].mean()).round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (((df['education'] == 'Bachelors').sum()/len(df['education']))*100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate']).sum()
    lower_education = len(df['education'])-higher_education
    h_ed_rich = df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')].shape[0]
    l_ed_rich = df[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')].shape[0]
    # percentage with salary >50K
    higher_education_rich = ((h_ed_rich/higher_education)*100).round(1)
    lower_education_rich = ((l_ed_rich/lower_education)*100).round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    total_min_hour_workers = len(df[df['hours-per-week']==min_work_hours])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[(df['salary'] == '>50K') & (df['hours-per-week'] == min_work_hours)])

    rich_percentage = num_min_workers/total_min_hour_workers *100

    # What country has the highest percentage of people that earn >50K?
    total_count_of_people = df['native-country'].value_counts()
    rich_people_country = df[(df['salary']=='>50K')]['native-country'].value_counts()
    percent_of_rich = rich_people_country/total_count_of_people *100
    highest_earning_country = percent_of_rich.idxmax()
    highest_earning_country_percentage = (percent_of_rich.max()).round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    indian_people = df[df['native-country'] == 'India']
    rich_indian_people = indian_people[indian_people['salary'] == '>50K']
    top_IN_occupation = rich_indian_people['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
