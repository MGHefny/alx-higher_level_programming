#!/bin/bash
#request to 0.0.0.0:5000/catch_me
curl -sLX PUT -H 'X-School-User-Id' -d 'user_id=98' 0.0.0.0:5000/catch_me
