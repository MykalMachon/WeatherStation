$HOST = ""
$PORT = ""

# launch meteor
cd ./meteor/
gunicorn main:app --bind <REPLACE_WITH_HOST> -k uvicorn.workers.UvicornWorker &

# return home 
cd ../

# launch station 
cd ./station/
HOST=$HOST PORT=$PORT node ./dist/server/entry.mjs