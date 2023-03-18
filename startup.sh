# setup variables
source ./meteor/venv/bin/activate

# launch meteor
python3 ./meteor/ & 

# launch station 
cd ./station/
HOST=$HOST PORT=$PORT node ./dist/server/entry.mjs