# aws-utilities

## auto-tag-users

This utility purpose is set the tag on IAM user with Key: email and Value: \<username\>@\<domain\>.

There is a TOML config file with 3 sections:

* [aws] - here you will set aws credentials and default region
* [email] - here you will set domain fro email address
* [account] - here you will set list of accounts to iterate thru and set email address tags to IAM users.

You can run this utility with python3.x binary. You need to have following libraries installed:

* boto3
* toml

Another option is to run it as docker container (obviously you need docker for that).

Just run:
```
bash$ sh local-run.sh
