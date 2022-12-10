


#To develop
- open with vs code 
- click the button at the bottom left
- select reopen from container
- then select the python_sdk.dockerfile

#To test / debug
- check .vscode/launch.json and veriy the parameters to fit the test you want to do
- through the debug tab, select the method you want to test and start debugging


#To run the container as it should be 

```
#this builds the docker image and tags it as 'transform'
docker build -t transform -f comax_transform.dockerfile .
#this runs the docker image and removes it automatically when shutting down
docker run --rm -v [fullpath]\test_data\ConfigureInput.json:/data/config.json  transform
```