# gitcdn

this is a simple **state less API** to replace of some github *API*


### Description

every time you want to upload some files to one of your github repository
you will need to use your own Github token. and if you want to let
other people to upload files to your Github repository, they will
need your token too. this project solves this problem, it will
provide some end point which let others to upload files to your
Github repository without your Github token.


### Environment Variables

| Name | Type |Description|
|:----:|:----:|:---------:|
|`SAVE_TO_DB`|bool|Indicate save the file to db or not|
|`REPO`|[str, ...]|list of REPO you have the access to|
|`OWNER`|str|the owner of the repositories|
|`TOKEN`|str|your Github token|


### Run testing server

```bash
# clone the repo
$ git clone https://github.com/shabane/gitcdn_prj.git && cd gitcdn_prj

# create & activate virtual environment
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requerment.txt

# set enironment varialbels
$ export REPO='CDN'
$ export OWNER='test'
$ export TOKEN='gpg_....'

# run test server
$ ./manage.py runserver 80
```
