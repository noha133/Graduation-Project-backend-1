package com.example.smart_edu.model;

public class User {
    private int id;
    private String username;
    private String password;
    private String token;


    public User(int id, String username, String password, String token) {
        this.id = id;
        this.username = username;
        this.password = password;
        this.token = token;
    }


    public int getId(){
        return id;
    }

    public void setId(int id){
        this.id = id;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public String getToken(){
        return token;
    }

}