from ingestion_service.sync_manager import SyncManager


def main():

    manager = SyncManager()

    manager.synchronize()


if __name__ == "__main__":

    main()