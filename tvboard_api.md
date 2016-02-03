FORMAT: 1A

# Tvboard

## Requestnumber [/api/v1/requestnumber/]
Get shanbay real time request number

### Retrieve Request number [GET]

+ Response 200 (application/json)

    + Body

        {
            ['key': 2016-01-14T02:15:15Z 
             'key_of_string': '2014-04-14T02:15:15Z'
             'doc_count': 100  
            ],
            ... 
        } 

## Checkin [/api/v1/checkin/]
Get shanbay checkin and platform rate

### Retrieve Checkin and Platform [GET]

+ Response 200 (application/json)

    + Body

        {
            'platform': 
                {
                    'ios': 43.5,
                    'android': 45.9,
                },
            'coordinates':
                {
                    [
                        {
                            'geoCoord':
                                {[
                                    105.0, 35.0
                                ]} 
                            'count': 8
                        },
                    ],
                    ...
                }
        }

## Quote [/api/v1/quote/]
Get shanbay quote

### Retrieve Quote [GET]

+ Response 200 (application/json)

    + Attributes
        + author (string) - author name
        + en (string) - English
        + zh (string) - Chinese

    + Body

        {
            'author': 'mary',
            'en': 'china',
            'zh': '中国’
        }

## Weather [/api/v1/weather/]
Get weather temperature city and aqi

### Retrieve Weather [GET]

+ Response 200 (application/json)

    + Body

        {
            'temperature': '-3～3℃',
            'city': '南京'，
            ’aqi': '149'
        }

## Bus [/api/v1/bus/]
Get real time bus

### Retrieve Bus [GET]

+ Response 200 (application/json)

    + Body

        {
            'to_xianling': 
                [7, 2],
            'to_xinmofan': 
                [13, 15]
        }

## Freshman [/api/v1/freshman/]
Get shanbay freshman within one month

### Retrieve Freshman [GET]

+ Response 200 (application/json)

    + Body

        [
            {
                'name': 'mary',
                'department': 'Operation',
                'photo': '/media/photo/mary.jpg'
            },
            ...
        ]

## Birthday [/api/v1/birthday/]
Get shanbay this month birthday

### Retrieve Birthday [GET]

+ Response 200 (application/json)

    + Body

        [
            {
                'name': 'mary',
                'department': 'Operation',
                'photo': '/media/photo/mary.jpg'
            },
            ...
        ]

## Bulletin [/api/v1/bulletin/]
Get company bulletin 

### Retrieve Bulletin [GET]

+ Response 200 (application/json)

    + Body

        [
            {
                'content': 'have a party',
                'location': 'office',
                'time': 2016.2.01 18:30
            }
            ...
        ]

