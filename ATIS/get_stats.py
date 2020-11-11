import os
import sys

slot_tag_counter = {
    "B-aircraft_code": 0,
    "B-airline_code": 0,
    "B-airline_name": 0,
    "B-airport_code": 0,
    "B-airport_name": 0,
    "B-arrive_date.date_relative": 0,
    "B-arrive_date.day_name": 0,
    "B-arrive_date.day_number": 0,
    "B-arrive_date.month_name": 0,
    "B-arrive_date.today_relative": 0,
    "B-arrive_time.end_time": 0,
    "B-arrive_time.period_mod": 0,
    "B-arrive_time.period_of_day": 0,
    "B-arrive_time.start_time": 0,
    "B-arrive_time.time": 0,
    "B-arrive_time.time_relative": 0,
    "B-booking_class": 0,
    "B-city_name": 0,
    "B-class_type": 0,
    "B-compartment": 0,
    "B-connect": 0,
    "B-cost_relative": 0,
    "B-day_name": 0,
    "B-day_number": 0,
    "B-days_code": 0,
    "B-depart_date.date_relative": 0,
    "B-depart_date.day_name": 0,
    "B-depart_date.day_number": 0,
    "B-depart_date.month_name": 0,
    "B-depart_date.today_relative": 0,
    "B-depart_date.year": 0,
    "B-depart_time.end_time": 0,
    "B-depart_time.period_mod": 0,
    "B-depart_time.period_of_day": 0,
    "B-depart_time.start_time": 0,
    "B-depart_time.time": 0,
    "B-depart_time.time_relative": 0,
    "B-economy": 0,
    "B-fare_amount": 0,
    "B-fare_basis_code": 0,
    "B-flight": 0,
    "B-flight_days": 0,
    "B-flight_mod": 0,
    "B-flight_number": 0,
    "B-flight_stop": 0,
    "B-flight_time": 0,
    "B-fromloc.airport_code": 0,
    "B-fromloc.airport_name": 0,
    "B-fromloc.city_name": 0,
    "B-fromloc.state_code": 0,
    "B-fromloc.state_name": 0,
    "B-meal": 0,
    "B-meal_code": 0,
    "B-meal_description": 0,
    "B-mod": 0,
    "B-month_name": 0,
    "B-or": 0,
    "B-period_of_day": 0,
    "B-restriction_code": 0,
    "B-return_date.date_relative": 0,
    "B-return_date.day_name": 0,
    "B-return_date.day_number": 0,
    "B-return_date.month_name": 0,
    "B-return_date.today_relative": 0,
    "B-return_time.period_mod": 0,
    "B-return_time.period_of_day": 0,
    "B-return_time.period_of_day ": 0,
    "B-round_trip": 0,
    "B-state_code": 0,
    "B-state_name": 0,
    "B-stoploc.airport_code": 0,
    "B-stoploc.airport_name": 0,
    "B-stoploc.city_name": 0,
    "B-stoploc.state_code": 0,
    "B-time": 0,
    "B-time_relative": 0,
    "B-today_relative": 0,
    "B-toloc.airport_code": 0,
    "B-toloc.airport_name": 0,
    "B-toloc.city_name": 0,
    "B-toloc.country_name": 0,
    "B-toloc.state_code": 0,
    "B-toloc.state_name": 0,
    "B-transport_type": 0,
    "I-airline_name": 0,
    "I-airport_name": 0,
    "I-arrive_date.day_number": 0,
    "I-arrive_time.end_time": 0,
    "I-arrive_time.period_of_day": 0,
    "I-arrive_time.start_time": 0,
    "I-arrive_time.time": 0,
    "I-arrive_time.time_relative": 0,
    "I-city_name": 0,
    "I-class_type": 0,
    "I-cost_relative": 0,
    "I-depart_date.day_number": 0,
    "I-depart_date.today_relative": 0,
    "I-depart_time.end_time": 0,
    "I-depart_time.period_of_day": 0,
    "I-depart_time.start_time": 0,
    "I-depart_time.time": 0,
    "I-depart_time.time_relative": 0,
    "I-economy": 0,
    "I-fare_amount": 0,
    "I-fare_basis_code": 0,
    "I-flight_mod": 0,
    "I-flight_number": 0,
    "I-flight_stop": 0,
    "I-flight_time": 0,
    "I-fromloc.airport_name": 0,
    "I-fromloc.city_name": 0,
    "I-fromloc.state_name": 0,
    "I-meal_code": 0,
    "I-meal_description": 0,
    "I-restriction_code": 0,
    "I-return_date.date_relative": 0,
    "I-return_date.day_number": 0,
    "I-return_date.today_relative": 0,
    "I-round_trip": 0,
    "I-state_name": 0,
    "I-stoploc.city_name": 0,
    "I-time": 0,
    "I-today_relative": 0,
    "I-toloc.airport_name": 0,
    "I-toloc.city_name": 0,
    "I-toloc.state_name": 0,
    "I-transport_type": 0,
    "O": 0,
}


def remove_digits(list):
    ret = []
    idx = []
    for i, item in enumerate(list):
        if not item.isdigit():
            ret.append(item)
        else:
            idx.append(i)
    return ret, idx


def replace_digits_with_DIGIT(list):
    ret = []
    idx = []
    for i, item in enumerate(list):
        if item.isdigit():
            ret.append("DIGIT")
            idx.append(i)
        else:
            ret.append(item.strip())
    return ret, idx


def main():
    wc = 0
    vocab = set()
    for filename in sys.argv[1:]:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                words = line.split('\t')[0].strip().split(' ')[1:-1]
                tags = line.split('\t')[1].strip().split(' ')[1:-1]
                # filtered_words, idx = remove_digits(words)
                filtered_words, idx = replace_digits_with_DIGIT(words)
                if len(filtered_words) != len(tags):
                    print(filtered_words)
                    print(tags)
                    raise ValueError(
                        'Number of words and tags must be the sames')
                wc += len(filtered_words)
                for word in filtered_words:
                    if word.strip() not in vocab:
                        vocab.add(word.strip())
                for tag in tags:
                    try:
                        slot_tag_counter[tag.strip()] += 1
                    except KeyError:
                        print(tag)

    print("word count: ", wc)
    print("vocab size: ", len(vocab))

    with open("slot_tag_count.txt", 'w', encoding='utf-8') as output_file:
        for item in sorted(slot_tag_counter.items(),
                              key=lambda x: x[0]):
            output_file.write(f'{item}\n')

    with open("vocab.txt", 'w', encoding='utf-8') as output_file:
        for word in sorted(list(vocab)):
            output_file.write(f'{word}\n')


if __name__ == '__main__':
    main()
