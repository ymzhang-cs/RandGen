from flask import Flask, request, render_template
from functions.rand import randGenerate
from hashlib import sha256


app = Flask(__name__)

@app.route("/generate")
def generate():

    # Arguments
    nickname = request.args.get('n')
    lR = request.args.get('leftRange')
    rR = request.args.get('rightRange')
    non = request.args.get('non')
    # UUID = request.args.get('UUID')

    # Generate Random Numbers
    random_numbers, time_stamp = randGenerate(lR, rR, non)
    print(random_numbers, time_stamp)

    # Calculate HASH
    hash_data = str(time_stamp)+lR+rR+non+str(random_numbers)
    hash_gen = sha256(hash_data.encode()).hexdigest()
    #hash_gen = hash(str(time_stamp)+lR+rR+non+str(random_numbers))

    return render_template('gen_result.html',
                           nickname=nickname,
                           time_stamp=str(time_stamp),
                           lR=lR, rR=rR,
                           non=non,
                           random_numbers=str(random_numbers)[1:-1],
                           hash=hash_gen,
                           verified_status="No")

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
