from django.shortcuts import render_to_response, get_object_or_404
from ncgmp.config import GeoServerConfig
from ncgmp.models import GeoMap

def termMapping(req, geomapId):
    return render_to_response("terminology/term-mapping.jade", { "geomapId": geomapId })

def javascript(req, gmId, fileName):
    gm = get_object_or_404(GeoMap, pk=gmId)
    polys = gm.mapunitpolys_set.all()
    if polys.count() > 0:
        extent = polys.extent()
    else:
        extent = (-179, -80, 179, 80)
        
    context = {
        "gsconfig": GeoServerConfig(),
        "gm": gm,
        "left": extent[0],
        "right": extent[2],
        "top": extent[3],
        "bottom": extent[1]       
    }
    
    return render_to_response(fileName, context, mimetype="text/javascript")