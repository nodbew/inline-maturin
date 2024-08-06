import inline_maturin

def test_build():

    # ビルド
    inline_maturin.build_maturin_project('maturin_test/pymodtest')

    # 関数のチェック
    import pymodtest
    assert pymodtest.add_two(6) == 8

    return
