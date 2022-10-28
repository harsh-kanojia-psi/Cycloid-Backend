from flask_restx import Resource, reqparse
from math import cos, sin
import matplotlib as m
import numpy as np
import matplotlib.pyplot as plt
from Models.input import inputModel


class Input(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('radius',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('del_dist',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )


    def get(self,plot_key):
        data = Input.parser.parse_args()

        input = inputModel.find_by_key(plot_key)
        if input:
            if input.del_dist > 2 * 3.14 * input.radius:
                return "Starting point must be on the circumference of the circle"

            else:
                try:
                    x_c = []
                    y_c = []
                    for theta in np.linspace(input.del_dist, 2 * 3.14 * input.radius):
                        x_c.append(input.radius * (theta - sin(theta)))
                        y_c.append(input.radius * (1 - cos(theta)))
                    plt.plot(x_c, y_c), plt.show()
                except:
                    return "bad request", 400


class saveData(Resource):

    def post(self):
        data = Input.parser.parse_args()

        input = inputModel(**data)

        if input.del_dist > 2*3.14*input.radius:
            return "Starting point must be on the circumference of the circle"

        else:
            try:
                input.save_to_db()
            except:
                return {"message": "An error occurred saving the user."}, 500
            return input.plotId()




