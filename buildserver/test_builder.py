import buildserver.builder


def test_list_assets():
    output = buildserver.builder.list_assets()
    assert len(output) == 13 # <= 13 assets total
    assert len(output[0]) == 2 # <= each line in the output should be (build, image)


def test_get_asset():
    output = buildserver.builder.get_asset("ci-main-3233")
    assert output == "asset: 1234.dkr.ecr.us-east-1.amazonaws.com/energyhub/dotcom:324"
