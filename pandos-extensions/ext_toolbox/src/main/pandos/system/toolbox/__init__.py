try:
    import pandos
except ImportError:
    raise ImportError(
        "Pandos is required to run this extension! "
        "Please be sure pandos is available in the runtime."
    )
