package com.example.smartedu.model;

import java.io.Serializable;

public class Users implements Serializable {
    private int pk;
    private String first_name;
    private String last_name;
    private String email;
    private String username;
    private String user_type;

    public Users(int pk, String username, String email, String firstname, String lastname) {
        this.pk = pk;
        this.email=email;
        this.username=username;
        this.first_name=firstname;
        this.last_name=lastname;
    }

    public String getUser_type() {
        return user_type;
    }

    public void setUser_type(String user_type) {
        this.user_type = user_type;
    }

    public String getFirst_name() {
        return first_name;
    }

    public String getLast_name() {
        return last_name;
    }

    public String getEmail() {
        return email;
    }

    public String getUsername() {
        return username;
    }


    public int getPk() {
        return pk;
    }
}
