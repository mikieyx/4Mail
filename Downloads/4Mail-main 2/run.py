from app import myapp_obj, socketio

# Run our Flask application:
#myapp_obj.run(debug=True)


if __name__ == "__main__":
    socketio.run(myapp_obj, debug=True)