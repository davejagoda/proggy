#!/bin/bash

aws route53domains list-domains --region us-east-1 | grep DomainName
