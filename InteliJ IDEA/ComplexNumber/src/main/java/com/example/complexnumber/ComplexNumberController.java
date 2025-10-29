package com.example.complexnumber;

import javafx.event.ActionEvent;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

public class ComplexNumberController {
    @javafx.fxml.FXML
    private Label result;
    @javafx.fxml.FXML
    private TextField firstCnumber;
    @javafx.fxml.FXML
    private TextField secondInumber;
    @javafx.fxml.FXML
    private TextField secondCnumber;
    @javafx.fxml.FXML
    private TextField firstInumber;

    @javafx.fxml.FXML
    public void add(ActionEvent actionEvent) {
        ComplexNumber c1, c2, c3;
        c1 = new ComplexNumber(Integer.parseInt(firstCnumber.getText()), Integer.parseInt(firstInumber.getText()));
        c2 = new ComplexNumber(Integer.parseInt(secondCnumber.getText()), Integer.parseInt(secondInumber.getText()));
        c3 = c1.add(c2);
        result.setText(c3.toString());
    }

    @javafx.fxml.FXML
    public void subtract(ActionEvent actionEvent) {
        ComplexNumber c1, c2, c3;
        c1 = new ComplexNumber(Integer.parseInt(firstCnumber.getText()), Integer.parseInt(firstInumber.getText()));
        c2 = new ComplexNumber(Integer.parseInt(secondCnumber.getText()), Integer.parseInt(secondInumber.getText()));
        c3 = c1.minus(c2);
        result.setText(c3.toString());
    }
}
