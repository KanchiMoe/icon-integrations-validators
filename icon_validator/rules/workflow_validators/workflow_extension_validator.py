from icon_validator.rules.validator import KomandPluginValidator


class WorkflowExtensionValidator(KomandPluginValidator):

    @staticmethod
    def validate_extension(extension):
        if not extension == 'workflow':
            raise Exception('Extension key must be workflow.')

    @staticmethod
    def validate_extension_exists(spec):
        if 'extension' not in spec.spec_dictionary():
            raise Exception('Workflow extension is missing.')

    def validate(self, spec):
        WorkflowExtensionValidator.validate_extension_exists(spec)
        WorkflowExtensionValidator.validate_extension(spec.spec_dictionary()['extension'])
