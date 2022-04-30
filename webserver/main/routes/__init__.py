import os
from flask_restplus import Api as BaseAPI

from main.routes.login import login_namespace


class Api(BaseAPI):
    def _register_doc(self, app_or_blueprint):
        # HINT: This is just a copy of the original implementation with the last line commented out.
        if self._add_specs and self._doc:
            # Register documentation before root if enabled
            app_or_blueprint.add_url_rule(self._doc, 'doc', self.render_doc)
        #app_or_blueprint.add_url_rule(self._doc, 'root', self.render_root)

    @property
    def base_path(self):
        return ''

api = Api(
    title='FairMatic API',
    version='1.0',
    description='Rest api for fairmatic dashboard project',
    doc='/swagger/' if os.getenv("ENV") != None else False
)

# api.render_root()

api.add_namespace(login_namespace, path='/v1/api')
