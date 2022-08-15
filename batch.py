"""A script for importing GeoPackage files into GeoServer"""

import argparse
import sys

from geopackage import get_layer_info, GeoPackageError
from geoserver import GeoServer, GeoServerError, LayerInfo

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Import GeoPackage files into GeoServer.')
    parser.add_argument('files', type=str, nargs='+',
                        help='one or more .gpkg files to import')
    parser.add_argument('-H', '--host', dest='host', type=str, action='store',
                        default="localhost:8080", help='the GeoServer host')
    parser.add_argument('-u', '--username', dest='username', type=str, action='store',
                        default="admin", help='the GeoServer user')
    parser.add_argument('-p', '--password', dest='password', type=str, action='store',
                        default="geoserver", help='the GeoServer password')
    parser.add_argument('-w', '--workspace', dest='workspace', type=str, action='store',
                        help='the GeoServer host')
    parser.add_argument('-s', '--secure', dest='secure', action='store_true',
                        default=False, help='whether GeoServer is using HTTPS')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
                        default=False, help='show verbose output')

    args = parser.parse_args()
    gs = GeoServer(
        host=args.host,
        username=args.username,
        password=args.password,
        secure=args.secure,
        workspace=args.workspace)

    try:
        for filename in args.files:
            infos = get_layer_info(filename)
            for info in infos:
                with open(filename, mode='rb') as f:
                    gs.ingest_store(info.table_name, info.data_type, f)
                url = gs.get_layer_image(LayerInfo(info.table_name, info.bounds, info.srs))
                if args.verbose:
                    print(url)

    except (GeoPackageError, GeoServerError) as e:
        print(f"Error: {e}", file=sys.stderr)
