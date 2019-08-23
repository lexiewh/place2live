import pandas as pd

df = pd.read_csv("city/output/list_of_countries.csv")


def run_country_checker():
    """Checks for a valid country by checking df"""
    while True:
        try:
            country = input("What is your country? ")
            country = country.lower()
            country = country.title()
            float(df[df.country == country]["purchasing_power_index"])
        except TypeError:
            print(f"'{country}' is an invalid country. Please try again.")
        else:
            return country


YOUR_COUNTRY = run_country_checker()


def _value_checker(index_input):
    """Helper function to input check the main index functions"""
    if index_input == '':   # empty string, default index
        return "default"
    try:
        return float(index_input)
    except ValueError:
        return False


def purchase_power_func():
    """finds your purchase power index"""
    country_purchasing_power_index = float(
        df[df.country == YOUR_COUNTRY]["purchasing_power_index"]
    )
    print(
        f"In your country purchasing power "
        f"index is {country_purchasing_power_index}"
    )

    while True:
        index_input = (input(
            "What is your desirable "
            "purchasing power index (higher is better)? ")
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_purchasing_power_index
        print(f"'{index_input}' is an invalid index. Please try again.")


def safety_func():
    """finds your safety index"""
    country_safety_index = float(
        df[df.country == YOUR_COUNTRY]["safety_index"]
    )
    print(
        f"In your country safety index is {country_safety_index}"
    )

    while True:
        index_input = (input(
            "What is your desirable safety index (higher is better)? ")
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_safety_index
        print(f"'{index_input}' is an invalid index. Please try again.")


def health_care_func():
    """finds your health care index"""
    country_health_care_index = float(
        df[df.country == YOUR_COUNTRY]["health_care_index"]
    )
    print(
        f"In your country health care index is {country_health_care_index}"
    )

    while True:
        index_input = (input(
            "What is your desirable health care index (higher is better)? ")
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_health_care_index
        print(f"'{index_input}' is an invalid index. Please try again.")


def climate_func():
    """finds your climate index"""
    country_climate_index = float(
        df[df.country == YOUR_COUNTRY]["climate_index"]
    )
    print(
        f"In your country climate index is {country_climate_index}"
    )

    while True:
        index_input = (input(
            "What is your desirable climate index (higher is better)? ")
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_climate_index
        print(f"'{index_input}' is an invalid index. Please try again.")


def cost_of_living_func():
    """finds your cost of living index"""
    country_cost_of_living_index = float(
        df[df.country == YOUR_COUNTRY]["cost_of_living_index"]
    )
    print(
        f"In your country cost of living "
        f"index is {country_cost_of_living_index}"
    )

    while True:
        index_input = (input(
            "What is your desirable cost of "
            "living index (lower is better)? ")
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_cost_of_living_index
        print(f"'{index_input}' is an invalid index. Please try again.")


def property_price_to_income_ratio_func():
    """finds your property price to income ratio index"""
    country_property_price_to_income_ratio = float(
        df[df.country == YOUR_COUNTRY]["property_price_to_income_ratio"]
    )
    print(
        f"In your country house price to "
        f"income ratio index is {country_property_price_to_income_ratio}"
    )

    while True:
        index_input = (input(
            "What is your desirable house price "
            "to income ratio (lower is better)? ")
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_property_price_to_income_ratio
        print(f"'{index_input}' is an invalid index. Please try again.")


def traffic_commute_time_func():
    """finds your traffic commute time index"""
    country_traffic_commute_time_index = float(
        df[df.country == YOUR_COUNTRY]["traffic_commute_time_index"]
    )
    print(
        f"In your country traffic commute time "
        f"index is {country_traffic_commute_time_index}"
    )

    while True:
        index_input = (input(
            "What is your desirable traffic commute "
            "time index (lower is better)? ")
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_traffic_commute_time_index
        print(f"'{index_input}' is an invalid index. Please try again.")


def pollution_func():
    """finds your pollution index"""
    country_pollution_index = float(
        df[df.country == YOUR_COUNTRY]["pollution_index"]
    )
    print(
        f"In your country pollution index is {country_pollution_index}"
    )

    while True:
        index_input = (input(
            "What is your desirable pollution index (lower is better)? ")
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_pollution_index
        print(f"'{index_input}' is an invalid index. Please try again.")


values = {
    "purchasing_power_index": 200,
    "safety_index": 200,
    "health_care_index": 200,
    "cost_of_living_index": 0,
    "property_price_to_income_ratio": 0,
    "traffic_commute_time_index": 0,
    "pollution_index": 0,
    "climate_index": 200,
}
df = df.fillna(value=values)


if __name__ == "__main__":
    your_purchasing_power_index = float(purchase_power_func())
    your_safety_index = float(safety_func())
    your_health_care_index = float(health_care_func())
    your_climate_index = float(climate_func())
    your_cost_of_living_index = float(cost_of_living_func())
    your_property_price_to_income_ratio = float(property_price_to_income_ratio_func())
    your_traffic_commute_time_index = float(traffic_commute_time_func())
    your_pollution_index = float(pollution_func())

    out_df = df[(df.purchasing_power_index > your_purchasing_power_index) &
                (df.safety_index > your_safety_index) &
                (df.health_care_index > your_health_care_index) &
                (df.cost_of_living_index < your_cost_of_living_index) &
                (df.property_price_to_income_ratio <
                    your_property_price_to_income_ratio) &
                (df.traffic_commute_time_index <
                    your_traffic_commute_time_index) &
                (df.pollution_index < your_pollution_index) &
                (df.climate_index > your_climate_index)]

    print_out_df = out_df[
        ["country", "freedomhouse_score", "quality_of_life_index"]
    ].dropna().sort_values(by=['freedomhouse_score'], ascending=False)

    if print_out_df.empty:
        print(f"There is no country better than {YOUR_COUNTRY}.")
    else:
        with pd.option_context("display.max_rows", None, "display.max_columns", None):
            print(print_out_df)
