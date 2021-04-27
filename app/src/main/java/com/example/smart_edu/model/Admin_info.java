package com.example.smartedu.model;

public class Admin_info {
    private String name;
    private String department;
    private int pk;

    public Admin_info(int pk, String name, String department){
        this.department = department;
        this.pk = pk;
        this.name = name;
    }

    public int getPk(){
        return pk;
    }

    public String getName() {
        return name;
    }

    public String getDepartment() {
        return department;
    }
}
