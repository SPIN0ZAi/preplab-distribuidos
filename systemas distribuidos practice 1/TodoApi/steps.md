## **DOCKER FILE**



FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build



WORKDIR /TodoApi



COPY . ./



RUN dotnet restore



RUN dotnet publish TodoApi.csproj -o out



FROM mcr.microsoft.com/dotnet/aspnet:10.0



WORKDIR /TodoApi



COPY --from=build /TodoApi/out .



ENV ASPNETCORE\_HTTP\_PORTS=8080



EXPOSE 8080



ENTRYPOINT \["dotnet", "TodoApi.dll"]





## **COMMANDS TO BUID**

## 

##### docker build -t todoapi .

##### 


**Run the container**
---



**docker run -d -p 5208:8080 --name todoapi-container todoapi**

## 

## **Check the API**



**http://localhost:5208**

**http://localhost:5208/swagger**



**Your complete workflow**



**You can think of the whole exercise as these four commands:**



**Build**

**docker build -t todoapi .**

**Run**

**docker run -d -p 5208:8080 --name todoapi-container todoapi**

**Check**

**docker ps**

**Test**

**http://localhost:5208**



**And later, when you do Ejercicio 4, the web frontend should point to:**



**http://localhost:5208**



**rather than 8080, because the browser is talking to the host, while Docker internally forwards 5208 → 8080.**

