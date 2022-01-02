from flask import Flask
from flask_wtf import FlaskForm
from wtforms import (
    PasswordField, StringField, IntegerField, EmailField, HiddenField, 
    SelectField, TextAreaField, BooleanField, FloatField, SubmitField)
from wtforms.validators import InputRequired, Length, Email, ValidationError, NumberRange


class RegistrationForm(FlaskForm):
    """
    Registration form class for our registration page
    """
    username = StringField('Username', validators=[InputRequired(),
        Length(min=6, max=30)])
    email = EmailField('Email', validators=[InputRequired(),
        Length(min=6, max=30)])
    password = PasswordField('Password', validators=[InputRequired(),
        Length(min=6, max=30)])


class LoginForm(FlaskForm):
    """
    Login form class for our login page
    """
    email = EmailField('Email', validators=[InputRequired(),
        Length(min=6, max=30)])
    password = PasswordField('Password', validators=[InputRequired(),
        Length(min=6, max=30)])


class AddWorkout(FlaskForm):
    """
    Form class to add new workouts
    """

    workout_name = StringField('Workout name:')
    exercise_name = SelectField('exercise:', validators=[InputRequired()])
    sets = IntegerField('sets:', validators=[InputRequired(),
        NumberRange(1, 20, message='Choose a value between 1 and 20')])
    reps = IntegerField('reps:', validators=[InputRequired(),
        NumberRange(1, 200, message='Choose a value between 1 and 200')])
    weight = FloatField('weight:', validators=[InputRequired(),
        NumberRange(1, 500, message='Choose a value between 1 and 500')])
    comments = TextAreaField('comments:', validators=[InputRequired(), Length(
        min=8, max=300, message='Must be 8-300 characters long')])


class EditWorkout(FlaskForm):
    """
    Form class to edit existing workouts
    """

    workout_name = StringField('Workout name:')
    exercise_name = SelectField('exercise:', validators=[InputRequired()])
    sets = IntegerField('sets:', validators=[InputRequired(),
        NumberRange(1, 20, message='Choose a value between 1 and 20')])
    reps = IntegerField('reps:', validators=[InputRequired(),
        NumberRange(1, 200, message='Choose a value between 1 and 200')])
    weight = FloatField('weight:', validators=[InputRequired(),
        NumberRange(1, 500, message='Choose a value between 1 and 500')])
    comments = TextAreaField('comments:', validators=[InputRequired(), Length(
        min=8, max=300, message='Must be 8-300 characters long')])
    id = HiddenField("id")


class AddExercise(FlaskForm):
    exercise_name = StringField(
        'Exercise name:', validators=[InputRequired(), Length(
            min=4, max=30,
            message='Must be 4-30 characters long')])
