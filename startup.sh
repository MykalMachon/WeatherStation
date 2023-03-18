

# launch meteor
cd ./meteor/
gunicorn main:app --bind 192.168.1.73 -k uvicorn.workers.UvicornWorker &

# return home 
cd ../

# launch station 
cd ./station/
HOST=$HOST PORT=$PORT node ./dist/server/entry.mjs