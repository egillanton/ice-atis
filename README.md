# The ICE-ATIS dataset (Version 0.2)

The Icelandic translation of the ATIS (Airline Travel Information System) dataset.


## Introduciton
The ICE-ATIS dataset tries to be the Icelandic version of the ATIS (Airline Travel Information System) dataset.

The dataset was translated with the use of Machine Translation, Natural Language Processing, and Manual Translation.



#### An Example

Original sample from the ATIS dataset:
```
BOS a listing of all flights from boston to baltimore before 10 am on thursday EOS	O O O O O O O B-fromloc.city_name O B-toloc.city_name B-depart_time.time_relative B-depart_time.time I-depart_time.time O B-depart_date.day_name atis_flight
```

Extracted text:
```
a listing of all flights from boston to baltimore before 10 am on thursday
```

Google Machine Translated:
```
skrá yfir allt flug frá boston til baltimore fyrir klukkan 10 á fimmtudag 
```

Manual Edited:
```
lista yfir öll flug frá boston til baltimore fyrir klukkan 10 á fimmtudag 
```

Manual Labled Slot-tags and Intentions:
```
BOS lista yfir öll flug frá boston til baltimore fyrir klukkan 10 á fimmtudag EOS	O O O O O B-fromloc.city_name O B-toloc.city_name B-depart_time.time_relative B-depart_time.time I-depart_time.time O B-depart_date.day_name atis_flight
```

For the task of re-labeling the IOB slot-tags, the following text annotation tool was created and used:

**Text Annoation Tool:** [https://github.com/egillanton/flask-text-annotation-tool](https://github.com/egillanton/flask-text-annotation-tool)



## Dataset
The Original data set can be obtained from  [Kaggle](https://www.kaggle.com/siddhadev/atis-dataset-from-ms-cntk), but I will use [these](https://github.com/mohammedterry/slots_intents/tree/d5883be0e9bc477ff2b3976e4ede7f29ad183805/data) optained files, for a main reason that is already preprocessed into two, simple to work with files. We can stil use the [Kaggle](https://www.kaggle.com/siddhadev/atis-dataset-from-ms-cntk) files for refrenceing  when labeling the slot tags and intention. 


ATIS dataset:
```
$ wc  ATIS/*
893   21900  153924 ATIS/atis.test.w-intent.iob
4978  132312  900059 ATIS/atis.train.w-intent.iob
5871  154212 1053983 total
```

Sample:
```
$ head -1 ATIS/atis.test.w-intent.iob 
BOS i would like to find a flight from charlotte to las vegas that makes a stop in st. louis EOS        O O O O O O O O O B-fromloc.city_name O B-toloc.city_name I-toloc.city_name O O O O O B-stoploc.city_name I-stoploc.city_name atis_flight
```

ICE-ATIS dataset:
```
$ wc ICE-ATIS/ice_atis.train.w-intent.iob ICE-ATIS/ice_atis.test.w-intent.iob
4978  136516  954071 ICE-ATIS/ice_atis.train.w-intent.iob
893   23339  166491 ICE-ATIS/ice_atis.test.w-intent.iob
5871  159855 1120562 total
```


Sample:
```
$ head -1  ICE-ATIS/ice_atis.test.w-intent.iob
BOS ég væri til í að finna flug frá charlotte til las vegas sem stoppar í st. louis EOS O O O O O O O O O B-fromloc.city_name O B-toloc.city_name I-toloc.city_name O O O B-stoploc.city_name I-stoploc.city_name O     atis_flight
```