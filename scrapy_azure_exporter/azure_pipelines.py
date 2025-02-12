from scrapy_azure_exporter.azure_store import AzureFilesStore
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline


class AzurePipelineMixin:
    @classmethod
    def from_crawler(cls, settings):
        pipeline = super().from_crawler(settings)
        pipeline.STORE_SCHEMES.update(
            {
                "azure": AzureFilesStore.new(settings),
                "azurite": AzureFilesStore.new(settings),
            }
        )
        return pipeline


class AzureFilesPipeline(AzurePipelineMixin, FilesPipeline):
    pass


class AzureImagesPipeline(AzurePipelineMixin, ImagesPipeline):
    pass
