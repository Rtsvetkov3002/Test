import numpy
from flask import Flask, render_template, request
from gauss import gauss

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET'])
def root():
    global Size
    Size = request.args.get("size_set")
    if Size is None:
        pass
    else:
        Size = int(request.args.get("size_set"))
    print(Size)
    return render_template('base.html', Size = Size)

@app.route('/answer', methods=['Post', 'GET'])
def answer():
    global Size
    print(Size)
    coefs = []
    for i in range(Size):
        string_of_coefs = []
        for j in range(Size):
            string_of_coefs.append(float(request.args.get(f"coefs_cell_[{i}][{j}]")))
        coefs.append(string_of_coefs)
    print(coefs)

    bees = []
    for i in range(Size):
        bees.append(float(request.args.get(f"b_cell_[{i}]")))
    print(bees)

    a = numpy.array(coefs)
    b = numpy.array(bees)
    det = numpy.linalg.det(a)
    solution = gauss(a, b)
    print(solution)
    if det == 0:
        return render_template('base.html', Size = Size, answer = solution, det = round(det, 5), calculation_success=False)
    return render_template('base.html', Size = Size, answer = solution, det = round(det, 5), calculation_success=True)



if __name__ == '__main__':
    app.run()
