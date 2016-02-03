FORMAT: 1A

# Lottery API Root [/{code_name}/]
Lottery API entry point

This resource get user lottery status and campaign id.

+ Parameters
    + code_name (string) - campaign unique name

## Retrieve Lottery Entry Point [GET]

+ Response 200 (application/json)

    + Attributes
        + status (number) - 显示用户中奖状态
            -1: 本日未抽奖
            0: 未抽中1: 中了，过了兑奖时间
            1: 中了，过了兑奖时间
            2: 中了，还未填写信息
            3: 中了，手机已验证
            4: 中了，已填写全部信息
            5: 活动已过期
        + campaign_id (number) - 活动ID
            '': 活动已过期
            1: 正在进行的活动id


    + Body

        {
            'status': -1,
            'campaign_id': 1
        }

## Lottery [/api/v1/lottery/{id}/]
Get bool judgement winning or not

+ Parameters 
    + id (number, required) ... ID of the Lottery in the form of a hash.

### Retrieve lottery [GET]

+ Response 200 (application/json)

    + Attributes
        + status (boolean) - 判断是否中奖
            True: winning
            False: not winning

    + Body

        {
            'status': True
        }


## Send Valid Code [/api/v1/verify/?mobile=15513149587]
Send a code to mobile

+ Parameters
    + mobile(string, required) ... 

### Retrieve valid code [GET]

+ Response 200 (application/json)

    + Attributes
        + status (boolean) - 发送验证码是否成功
            True: send ok
            False: send false

    + Body

        {
            'status': True
        }


## Valid Code [/api/v1/verify/]
Valid mobile code 

### Retrieve Valid [PUT]

+ Attributes
    + mobile (string, required) - phone number
    + code (string, required) - phone valid code

+ Request (application/json)

+ Response 204 (application/json)

    + Attributes
        + status (boolean) - 是否验证成功
            True: valid success
            False: valid false

    + Body

        {
            'status': True
        }


## Add information [/api/v1/information/]
Add user name and address.

### Retrieve information [PUT]

+ Attributes
    + mobile (string, required) - phone number
    + name (string, required) - user name
    + address (string, required) - user address

+ Request (application/json)

+ Response 204 (application/json)

    + Attributes
        + status (boolean) - 是否插入数据成功
            True: valid success
            False: put false

    + Body

        {
            'status': True
        }


## Campaign Rules [/api/v1/info/{id}/]
Get Campaign rules

+ Parameters
    + id (number, required) - campaign id

### Retrieve Campaign info [GET]

+ Response 200 (application/json)

    + Body

        {
            'campaign': 
                {
                    'title': '2016',
                    'theme': 'apple',
                    'start_time': '2016-01-28T05:36:42Z',
                    'end_time': '2016-02-02T05:36:47Z',
                    'rules': 'one day one time'
                }
            'awards':
                {
                    [
                        'name': 'iphone',
                        'amount': 100,
                        'link': 'http://www.shanbay.com/iphone.jpg'
                    ]
                    ...
                }
        }

## Campaign Lists [/api/v1/campaigns/]
Get campaign lists

### Retrieve Campaign Lists [GET]

+ Response 200 (application/json)

    + Attributes
        + id (number) - campaign id
        + title (string) - campaign title

    + Body

       {
            [
                'id': 1,
                'title': 'apple'
            ]
            ...
        }

## Award Records [/api/v1/winnings/{id}/]
Get winnings information

+ Parameters
    +id (number, required) - campaign id

### Retrieve Wining Records [GET]

+ Response 200 (application/json)

    + Attributes
        + award_id (number) - award id
        + name (string) - user name
        + mobile (string) - user phone number
        + address (string) - user address
        + express (string) - user express

    + Body

        {
            [
                'award_id': 1,
                'name': 'mary',
                'mobile': '15513149587',
                'address': '南京',
                'express': '122345'
            ]
            ...
        }

