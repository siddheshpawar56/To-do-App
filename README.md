# To-do-App
You need to create a account on [Firebase](https://console.firebase.google.com/u/0/ "Firebase")
</br>
</br>Create a New Project on Firebase.After creating a project successfully create a new database.
</br></br>After creating a database to project settings.Scroll down and click on the web button.You will notice that they are credentials for the firebase.You need to copy and paste this credentials into the app.py file in config.
</br></br>
# Steps to Deploy
</br>
git clone the repo </br></br>
cd into the clone repo</br></br>
sudo docker build -t To-do-app:v1 .</br>[Note: Copy the whole line along with dot(.) while pasting it]</br></br>
sudo docker images </br>[Note: list the image that you have created]</br></br>
sudo docker run -it -d -p 8080:8080 --name=Todo_App To-do-app:v1 </br>[Note: Run the Application image with name Todo_App]</br></br>
sudo docker ps -a</br>
[Note: check if the container has been deployed and for other details like started,running,exited]</br></br>

# Test your Application 
write the below http link after changing the localhost or IP address on a web browser</br></br>
http://[localhost or IP address]:5000</br></br>

# Output


