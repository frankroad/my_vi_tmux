FORMAT: v1
HOST: http://www.shanbay.com/api/v1/

# API Name and Overview Section

这里是这一页 API 的相关描述，包括： 关于什么资源，什么操作

## Authentication

关于认证方式的说明，如果无需认证，不需要本节

## Error States

遵循 [HTTP Response Status Codes](https://github.com/for-GET/know-your-http-well/blob/master/status-codes.md) 标准.

# Group Resources

关于`resources`组的描述

## Resource [/resources/{id}]

关于`resource`资源的描述

+ Parameters
  + id: `3` (number, required) - id of the resource

### Get a Resource [GET]

+ Parameters
  + pretty (boolean, optional) - print json in pretty mode

+ Response 200 (application/json)
  + Headers
    Link: <http:/api.shanbay.com/>;rel="self",<http:/api.shanbay.com/resources>;rel="resources",<http:/api.shanbay.com/authorization>;rel="authorization"

  + Attributes (ResourceRead)

### Update a Resource [PUT]

+ Parameters
  + source (boolean, optional) - whether to return source data of the resource

+ Request (application/json)
  + Attributes (ResourcePayload)

+ Response 200 (application/json)
  + Attributes (ResourceRead)

+ Response 422 (application/json)
  + Attributes (ResourceError)

### Delete a Resource [DELETE]

+ Response 204 (application/json)


## Resources Collection [/teams]

关于`resources collection`资源的描述

### List Resources [GET]

+ Parameters
  + page: 0 (number, optional) - page of resource list
    + Default: 0
  + per_page: 10 (number, optional) - how many items per page
    + Default: 10
  + pretty (boolean, optional) - print json in pretty mode

+ Response 200 (application/json)
  + Headers
    Link: <http:/api.shanbay.com/>;rel="self",<http:/api.shanbay.com/resources>;rel="resources",<http:/api.shanbay.com/authorization>;rel="authorization"

  + Attributes (array[ResourceRead])

### Create a Resource [POST]

+ Request (application/json)
  + Attributes (ResourcePayload)

+ Response 201 (application/json)
  + Attributes (ResourceRead)

+ Response 422 (application/json)
  + Attributes (ResourceError)

# Data Structures

## ResourcePayload
+ content: `Content of this Resource` (string) - The blog post article
+ author (object)
  + name: `Michael Ding` (string) - name of the author
  + email: `yan.ding@shanbay.com` (string) - email of the author
  + location: `Jiangsu` (string, default) - location of the author
  + gender: `male`, `female` (enum) - gender of the author
    - Default: `male`

## ResourceRead (ResourcePayload)
+ id: `3` (number) - id of the resource
+ created_at: `2016-01-02T00:00:00Z` (string) - when the resource was created, in ISO8601 format
+ updated_at: `2016-01-02T00:00:00Z` (string) - when the resource was updated, in ISO8601 format

## ResourceError
+ message: `Bad Request` (string) - brief message of error
+ errors
  + content: `blank`, `illegal` (array[string])
  + author.name: `blank`, `parse error` (array[string])
  + author.email: `parse error` (array[string])
  + author.location: `illegal` (array[string])
  + author.gender: `mismatch` (array[string])
