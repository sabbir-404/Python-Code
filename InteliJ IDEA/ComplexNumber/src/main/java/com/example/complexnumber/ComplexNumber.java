package com.example.complexnumber;

public class ComplexNumber {
    int real;
    int img;

    public ComplexNumber(int img, int real) {
        this.img = img;
        this.real = real;
    }

    public ComplexNumber() {
    }

    public int getReal() {
        return real;
    }

    public void setReal(int real) {
        this.real = real;
    }

    public int getImg() {
        return img;
    }

    public void setImg(int img) {
        this.img = img;
    }

    @Override
    public String toString() {
        return real + " + " + img + 'i';
    }
    ComplexNumber add(ComplexNumber c){
        ComplexNumber temp = new ComplexNumber();
        temp.real= this.real + c.real;
        temp.img= this.img + c.img;
        return temp;
    }

    ComplexNumber minus(ComplexNumber c){
        ComplexNumber temp = new ComplexNumber();
        temp.real= this.real - c.real;
        temp.img= this.img - c.img;
        return temp;
    }
}
