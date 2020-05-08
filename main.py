from planar_rf.planar_rf import PlanarRF

def best_station(request):
    """HTTP Cloud Function returning the best link station for a given point.
    Args:
        request (flask.Request): The request object.
        Needs to contain the point as two query params x and y.
    Returns:
        The response as text/plain.
    """
    request_args = request.args
    try:
        x = int(request_args.get('x'))
        y = int(request_args.get('y'))
        if x is None or y is None:
            return "Missing query parameter(s) x and y", 400
    except:
        return "Invalid input", 400

    prf = PlanarRF()
    ret = prf.find_best_station((x,y))
    if ret is None:
        return "No link station within reach for point {}, {}".format(x, y)
    else:
        best_bs_x, best_bs_y, best_bs_pwr = ret
        return "Best link station for point {},{} is {},{} with power {}".format(x, y, best_bs_x, best_bs_y, best_bs_pwr)

