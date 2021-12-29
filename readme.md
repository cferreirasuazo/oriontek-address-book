
<div id="top"></div>
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
  </a>

  <h3 align="center">Address Book Readme</h3>

</div>


<!-- ABOUT THE PROJECT -->
## About The Project


The current project is build using Django webframework for it's development. The app is dockernize and seperated in web (Django App) and db (PostgresDB)


### Built With


This section lists the tecnologies used for this project: 


* [Django](https://www.djangoproject.com/)
* [Docker](https://www.docker.com/)
* [Postgres](https://www.postgresql.org/)
* [Bootstrap](https://getbootstrap.com/)


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

for getting started, you must have installed docker in your computer. 

### Installation



1. run docker build 
```
    docker-compose up --build
```

2. Once the containers are installed, search for the web container using:

```
    docker container ls
```

3. run migrations 

```
    docker exec -it [container_id] python manage.py migrate
```

4. Once the migrations are installed, the app should be running in 0.0.0.0:8000



<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Register user
- [x] login
- [x] addresses crud (create, read, update, delete)


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

* [Email](cferreirasuazo@gmail.com)
* [Github](https://github.com/cferreirasuazo)
* [Medium](https://cferreirasuazo.medium.com/)



