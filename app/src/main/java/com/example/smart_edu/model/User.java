package com.example.smartedu.model;

public class User {
    private String key;


    public User(String key) {
        this.key = key;
    }

    public String getToken(){
        return key;
    }

}
