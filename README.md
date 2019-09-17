# -restframe-blog-
前后端分离，cbv，加了频率，分页等


使用模块有：auth，restframework，等

blog功能：
  每个url都有访问频率，一分钟内访问几次，自己设置
        用户注册，（姓名，密码，头像上传（不上传文件，使用默认头像），手机号），
               注册成功
        用户登录，附带验证码
                1.成功：
                    {
                          "data": {
                              "nid": 5,
                              "username": "zmm6",
                              "phone": "123456",
                              "permissions": "普通用户",
                              "avatars": "/media/zmm6/avatar/timg.jpg",
                              "user_avatars": 1
                          },
                          "code": 100,
                          "error": null
                      }返回用户信息
                    2.失败进行提示哪里问题
        文章 ：增，删，改，查。都要判断用户是否正确等
              查：
                  查看全部文章：
                        {
                          "data": [
                              {
                                  "nid": 6,
                                  "title": "asdsad",
                                  "desc": "dsad",
                                  "create_time": "2019-09-16T09:36:03.497076Z",
                                  "up_count": 2,
                                  "down_count": 1,
                                  "comment_count": 2,
                                  "user": "zmm6"
                              }
                          ],
                          "code": 100,
                          "error": null
                      }
                     查看具体文章：
                     {
                      "data": {
                          "article_data": {
                              "nid": 6,
                              "title": "asdsad",
                              "desc": "dsad",
                              "create_time": "2019-09-16T09:36:03.497076Z",
                              "up_count": 2,
                              "down_count": 1,
                              "category": [
                                  {
                                      "category_id": 5,
                                      "category_name": "das"
                                  }
                              ],
                              "article_user": "zmm6",
                              "tags": [
                                  {
                                      "tag_id": 3,
                                      "title": "老板"
                                  }
                              ],
                              "content": "",
                              "comment": [
                                  {
                                      "comment_id": 3,
                                      "comment_content": "1dddaasds",
                                      "commentator": "zmm",
                                      "parent_id": null,
                                      "comment_time": "2019-09-16T09:36:24.589385Z",
                                      "comment_status": 1
                                  },
                                  {
                                      "comment_id": 5,
                                      "comment_content": "21131",
                                      "commentator": "zmm6",
                                      "parent_id": null,
                                      "comment_time": "2019-09-17T02:54:12.050662Z",
                                      "comment_status": 0
                                  }
                              ]
                          },
                          "all_tags": [],
                          "all_category": [
                              {
                                  "nid": 5,
                                  "title": "das",
                                  "category_count": 2
                              },
                              {
                                  "nid": 6,
                                  "title": "悟空传",
                                  "category_count": 1
                              }
                          ]
                      },
                      "code": 100,
                      "error": null
                  }
                        
                        
              评论的删除，增加
              点赞的增加
