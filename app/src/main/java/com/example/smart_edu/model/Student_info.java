package com.example.smartedu.model;

public class Student_info {
    private  int user;
    private String name;
    private int semester_number;
    private int Class;

    public Student_info(int user, String name, int semester_number, int Class){
        this.name = name;
        this.user = user;
        this.Class = Class;
        this.semester_number = semester_number;
    }
    public int getUser() {
        return user;
    }

    public String getName() {
        return name;
    }

    public int getSemester_number() {
        return semester_number;
    }

    public int getClassname() {
        return Class;
    }

}
