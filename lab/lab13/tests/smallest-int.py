test = {
  'name': 'smallest-int',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int;
          7/30/2017 12:19:49|6
          7/30/2017 12:20:11|6
          7/30/2017 12:30:19|7
          7/30/2017 12:53:09|7
          7/30/2017 19:55:58|7
          7/30/2017 21:30:13|7
          7/30/2017 22:29:18|7
          7/28/2017 8:51:21|8
          7/30/2017 13:12:01|8
          7/30/2017 23:00:53|8
          7/31/2017 17:42:49|8
          7/30/2017 12:13:44|9
          7/30/2017 14:53:24|9
          7/30/2017 15:31:54|9
          7/31/2017 16:28:18|12
          7/30/2017 17:13:35|13
          7/30/2017 8:52:21|13
          7/30/2017 11:42:29|14
          7/30/2017 12:43:59|14
          7/30/2017 13:10:42|14
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
