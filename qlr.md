<details><summary>Commit History</summary>

```diff

+ commit 667042640686d985664130bb3b638b22b63454da
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Sat Dec 2 17:20:06 2023 -0600

    Working on recieving real time data into the pie chart

 expenseswebsite/static/js/financial/piechart.js | 4 +++-
 1 file changed, 3 insertions(+), 1 deletion(-)

+ commit b66e244ca535daade4a24a0364f389b0bab20fd6
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Fri Dec 1 22:12:09 2023 -0600

    added the pie chart to financial section

 expenseswebsite/static/js/financial/piechart.js    | 68 ++++++++++++++++++++++
 kpis/views.py                                      |  4 ++
 templates/kpis/edit_report.html                    |  4 +-
 .../financial/monthly_report_financial.html        | 19 +++++-
 .../kpis/reports/randr/edit_report_randr.html      |  4 +-
 .../kpis/reports/randr/monthly_report_randr.html   |  4 +-
 6 files changed, 96 insertions(+), 7 deletions(-)

+ commit f7f6e3830a3ddbd79b56190fde405dc879786975
Author: joshjetson <joshjetson@gmail.com>
- Date:   Fri Dec 1 17:02:57 2023 -0600

    The Financial report section is functional now. I worked out some problems with the pipeline and model relations

 .../static/js/financial/financial_line.js          |  28 +----
 kpis/migrations/0006_financial.py                  |  53 ++++++++
 kpis/models.py                                     |  59 +++++++++
 kpis/templatetags/getattribute.py                  |   2 +-
 kpis/views.py                                      | 110 +++++++++++++---
 templates/kpis/monthly_report.html                 |   4 +-
 .../reports/financial/edit_report_financial.html   | 139 +++++++++++++++++++-
 .../reports/financial/modify_report_financial.html |  65 ++++++++++
 .../financial/monthly_report_financial.html        | 140 ++++++++++++++++++++-
 9 files changed, 549 insertions(+), 51 deletions(-)

+ commit 2e6eb41b493f065527bd539185075069a1e82a85
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Wed Nov 29 17:54:12 2023 -0600

    Tackling the queryset issue

 kpis/views.py                                        | 19 ++++++++++++++++++-
 .../reports/financial/monthly_report_financial.html  | 20 ++++++++++++++++----
 2 files changed, 34 insertions(+), 5 deletions(-)

+ commit 05909101b10c7cb99eee3a043849fd1bd8100fbb
Author: joshjetson <joshjetson@gmail.com>
- Date:   Wed Nov 29 13:39:17 2023 -0600

    Made the migrations of the Financial Models and performed the migration

 .../0005_financial_revenue_financial_hours.py      | 78 ++++++++++++++++++++++
 1 file changed, 78 insertions(+)

+ commit 46fc1da6fc489e24e3c3baac56023c8c691b8279
Author: joshjetson <joshjetson@gmail.com>
- Date:   Wed Nov 29 13:37:18 2023 -0600

    Tackled many issues and am now focusing on the Financial Reports section

 expenseswebsite/static/css/bootstrap.css           |  3430 +++--
 expenseswebsite/static/css/bootstrap_morph.css     | 12750 +++++++++++++++++++
 expenseswebsite/static/js/dynamic_line.js          |   185 +
 .../{RandR_line.js => financial/financial_line.js} |   105 +-
 expenseswebsite/static/js/modular_line.js          |     8 +-
 expenseswebsite/static/js/randr/randr_line.js      |   211 +
 kpis/models.py                                     |    75 +
 kpis/urls.py                                       |     2 +-
 kpis/views.py                                      |   236 +-
 templates/assets/index.html                        |     8 +-
 templates/kpis/edit_report.html                    |     6 +-
 templates/kpis/modify_report.html                  |    16 +-
 templates/kpis/monthly_report.html                 |    22 +-
 .../reports/financial/edit_report_financial.html   |   297 +
 .../reports/financial/modify_report_financial.html |   127 +
 .../monthly_report_financial.html}                 |   166 +-
 .../kpis/reports/randr/edit_report_randr.html      |   297 +
 .../kpis/reports/randr/modify_report_randr.html    |   127 +
 .../kpis/reports/randr/monthly_report_randr.html   |   481 +
 templates/welcome.html                             |    31 +-
 20 files changed, 16545 insertions(+), 2035 deletions(-)

+ commit 18df797554e41b13ac5be2ce5c37b74b72d14a2a
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Wed Nov 22 16:49:05 2023 -0600

    Now Monthly Report and Edit Report are both Modular. Next is Modify Report

 kpis/templatetags/__init__.py     |  0
 kpis/templatetags/getattribute.py | 21 +++++++++++++++++++++
 kpis/views.py                     | 32 +++++++++++++++++++++++---------
 templates/index.html              |  1 +
 templates/kpis/edit_report.html   | 15 ++++++++-------
 5 files changed, 53 insertions(+), 16 deletions(-)

+ commit e6e27df4f035104c0772b7a4ced7e4b47f790c00
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Wed Nov 22 11:15:42 2023 -0600

    Made Repair

 kpis/views.py | 32 ++++++++++++++++----------------
 1 file changed, 16 insertions(+), 16 deletions(-)

+ commit 54f28c3d3f6c7e5afc29387f6dbfa3c5ec61a701
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Tue Nov 21 13:14:13 2023 -0600

    Modular pursuit

 kpis/views.py                   | 28 ++++++++++++++--------------
 metrics/monthly_report.md       | 30 +++++++++++++++++++++---------
 templates/kpis/edit_report.html | 12 ++++++------
 3 files changed, 41 insertions(+), 29 deletions(-)

+ commit c0884583c18f6cb516d8ebe1f1ef1c22bc433e92
Author: joshjetson <joshjetson@gmail.com>
- Date:   Tue Nov 21 08:58:51 2023 -0600

    Continuing the process of modularization

 expenseswebsite/static/js/RandR_line.js   | 208 +++++++++++++++
 expenseswebsite/static/js/modular_line.js |  66 ++---
 kpis/models.py                            |   9 +
 kpis/views.py                             | 129 +++++++--
 metrics/monthly_report.md                 |  61 ++++-
 templates/kpis/edit_report.html           |  26 +-
 templates/kpis/edit_report_backup.html    | 271 +++++++++++++++++++
 templates/kpis/monthly_report.html        | 230 +++++++++-------
 templates/kpis/monthly_report_copy.html   | 422 ++++++++++++++++++++++++++++++
 templates/kpis/reports/randr.html         | 131 ++++++----
 10 files changed, 1330 insertions(+), 223 deletions(-)

+ commit 15b1f5e2cf639e279a622fb5ccc2515ddef2795f
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Thu Nov 16 12:57:06 2023 -0600

    Refined many of the formulas

 metrics/monthly_report.md | 77 ++++++++++++++++++++++++++++++-----------------
 1 file changed, 50 insertions(+), 27 deletions(-)

+ commit b2f8524d01e0ca7b0321c0070a6575af945e0d34
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Wed Nov 8 13:24:33 2023 -0600

    Making it look like theirs_3

 expenseswebsite/static/css/paper.css       |   6 ++
 expenseswebsite/static/img/cap_lenders.png | Bin 0 -> 10035 bytes
 expenseswebsite/static/img/impossible.png  | Bin 0 -> 21305 bytes
 expenseswebsite/static/img/legal_help.png  | Bin 0 -> 3508 bytes
 expenseswebsite/static/img/work_adv.png    | Bin 0 -> 5404 bytes
 templates/base.html                        |   2 +-
 templates/index.html                       |   4 +-
 templates/indi_coaching.html               | 148 ++++++++++++++++++++++++++++
 templates/partials/sidebar.html            |   2 +-
 templates/partials/welcome_sidebar.html    |  10 +-
 templates/perf_groups.html                 |   8 +-
 templates/services.html                    |  20 ++--
 templates/trusted.html                     | 151 +++++++++++++++++++++++++++++
 userpreferences/views.py                   |   4 +
 14 files changed, 335 insertions(+), 20 deletions(-)

+ commit 8b9cbf790623d5d476be152989369522fff1393e
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Tue Nov 7 18:37:47 2023 -0600

    Making it look like theirs_2

 expenseswebsite/static/css/paper.css            |  10 +-
 expenseswebsite/static/img/favicon.png          | Bin 132418 -> 45010 bytes
 expenseswebsite/static/img/glass_writing.png    | Bin 0 -> 21585 bytes
 expenseswebsite/static/img/kpi_card_2.png       | Bin 0 -> 88158 bytes
 expenseswebsite/static/img/kpi_cards.png        | Bin 0 -> 107676 bytes
 expenseswebsite/static/img/kpi_favicon.xcf      | Bin 0 -> 185374 bytes
 expenseswebsite/static/img/kpi_middle.png       | Bin 0 -> 76159 bytes
 expenseswebsite/static/img/kpiqlogo.png         | Bin 0 -> 17211 bytes
 expenseswebsite/static/img/many_charts_neon.jpg | Bin 0 -> 103666 bytes
 expenseswebsite/static/img/meeting.png          | Bin 0 -> 27504 bytes
 expenseswebsite/static/img/pen_chart.png        | Bin 0 -> 26795 bytes
 expenseswebsite/static/img/perf_groups.png      | Bin 0 -> 323533 bytes
 expenseswebsite/static/img/stock_chart_dood.jpg | Bin 0 -> 93002 bytes
 expenseswebsite/static/img/support_pic.png      | Bin 0 -> 34716 bytes
 expenseswebsite/static/img/team.png             | Bin 0 -> 40430 bytes
 templates/index.html                            |  49 ++++---
 templates/kpi_metrics.html                      | 159 ++++++++++++++++++++
 templates/perf_groups.html                      | 139 ++++++++++++++++++
 templates/services.html                         | 183 ++++++++++++++++++++++++
 userpreferences/urls.py                         |   1 +
 userpreferences/views.py                        |   8 ++
 21 files changed, 529 insertions(+), 20 deletions(-)

+ commit 905f65f2622faf3c044d5666734e1d2e6e31c27f
Merge: 20c65c1 d041791
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Mon Nov 6 22:58:57 2023 -0600

    Merge remote-tracking branch 'origin/dev' into dev
    I messed up and didnt pull first

+ commit 20c65c1d656488b77e7ad864c835aad2528764e4
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Mon Nov 6 18:40:01 2023 -0600

    Making it look like theirs

 authentication/views.py                        |   4 +-
 expenseswebsite/settings.py                    |   6 +
 expenseswebsite/static/img/desk_worker.png     | Bin 0 -> 20214 bytes
 expenseswebsite/static/img/gears_.png          | Bin 0 -> 24122 bytes
 expenseswebsite/static/img/paper_resources.png | Bin 0 -> 23653 bytes
 landing.md                                     |  16 ++
 templates/index.html                           |  73 +++++--
 templates/kpis/monthly_report.html             |   1 -
 templates/partials/welcome_sidebar.html        |  41 ++++
 templates/welcome.html                         | 263 +++++++++++++++++++++++++
 userpreferences/urls.py                        |   1 +
 userpreferences/views.py                       |   5 +-
 12 files changed, 388 insertions(+), 22 deletions(-)

+ commit d0417912c68d13a658f0b601464a85b7b4270a10
Author: joshjetson <joshjetson@gmail.com>
- Date:   Fri Nov 3 11:45:17 2023 -0500

    minor updates

 kpis/views.py | 6 +++---
 steps.md      | 2 +-
 2 files changed, 4 insertions(+), 4 deletions(-)

+ commit 998d49b0b8c5524bd9c230b4a576630e8ec3ab2e
Author: Josh at Moms <josh@virtualraremedia.com>
- Date:   Tue Oct 31 15:25:55 2023 -0700

    Modular Lines are now dynamic

 code_count.txt                            | 186 ++++++++++++++++++++++++++++++
 expenseswebsite/static/js/modular_line.js |   2 +-
 kpis/urls.py                              |   2 +-
 kpis/views.py                             |  71 ++++++------
 templates/kpis/monthly_report.html        |   2 +-
 5 files changed, 224 insertions(+), 39 deletions(-)

+ commit 80d702f5d6e108f2e469addb4d8c853a97a974df
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Mon Oct 30 00:21:40 2023 -0500

    minor 5

 kpis/views.py | 7 ++++++-
 1 file changed, 6 insertions(+), 1 deletion(-)

+ commit 1abfa8c8f1ded03cb895040109d948a8c5545660
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Sun Oct 29 01:37:14 2023 -0500

    minor 4

 templates/kpis/reports/randr.html | 303 +++++++++-----------------------------
 1 file changed, 72 insertions(+), 231 deletions(-)

+ commit 4d0fbf807fdafb66603b55efdcae8ebb8cbac78b
Author: Josh at Moms <josh@virtualraremedia.com>
- Date:   Sat Oct 28 22:30:35 2023 -0700

    Dynamic Refactor of KPIs Completed

 kpis/views.py                      |  31 +++-
 templates/kpis/monthly_report.html | 293 +++++++++----------------------------
 2 files changed, 95 insertions(+), 229 deletions(-)

+ commit 28b27d2808e8d8068264d388077b021519baac03
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Sat Oct 28 10:41:36 2023 -0500

    Refactored some more and added RandR formula

 kpis/models.py |  13 +++++-
 kpis/urls.py   |   1 -
 kpis/views.py  | 133 +++++++++++++++++++++++++++++++++++++++++++--------------
 3 files changed, 113 insertions(+), 34 deletions(-)

+ commit f0157ba7264b0e10a5363ecd370a540033370200
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Fri Oct 27 19:32:11 2023 -0500

    formatting

 kpis/views.py | 11 ++++-------
 1 file changed, 4 insertions(+), 7 deletions(-)

+ commit 587a1a1c40273d61fbe0981c8b57d16018a18053
Author: Josh at Moms <josh@virtualraremedia.com>
- Date:   Fri Oct 27 16:08:51 2023 -0700

    Made most of kpi views dynamic so as this application scales it can handle the growth without having to type a bunch of the same code over and over

 ...randr_options_alter_reports_options_and_more.py |  31 +++
 kpis/models.py                                     |  15 +-
 kpis/urls.py                                       |   2 +-
 kpis/views.py                                      | 262 ++++++++++++---------
 templates/kpis/edit_report.html                    |   6 +-
 templates/kpis/modify_report.html                  |   2 +-
 6 files changed, 193 insertions(+), 125 deletions(-)

+ commit 8322b0215e1192878e2246db3b8450fca07fd028
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Thu Oct 26 17:24:20 2023 -0500

    Refactoring

 kpis/urls.py                                       |   6 +-
 kpis/views.py                                      | 123 ++++++++++-----------
 templates/base.html                                |   2 +-
 templates/index.html                               |   2 +-
 .../kpis/{edit_sales.html => edit_report.html}     |   2 +-
 templates/kpis/monthly_report.html                 |   6 +-
 templates/partials/sidebar.html                    |   2 +-
 7 files changed, 67 insertions(+), 76 deletions(-)

+ commit 7acbc30c2d021223e2c0523bc3c55524d38609d0
Author: Josh at Moms <josh@virtualraremedia.com>
- Date:   Wed Oct 25 10:15:18 2023 -0700

    condensing

 kpis/models.py | 12 ++++++++++++
 kpis/views.py  | 12 ++++++------
 2 files changed, 18 insertions(+), 6 deletions(-)

+ commit d10cd21175097efd13a878911577b363b3fb1780
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Tue Oct 24 11:51:49 2023 -0500

    important notes

 notes.md | 14 ++++++++++++++
 1 file changed, 14 insertions(+)

+ commit ce0863a2c94a56be97968b679d547806304d59ea
Author: Josh at Moms <josh@virtualraremedia.com>
- Date:   Tue Oct 24 09:38:20 2023 -0700

    --

 kpis/migrations/0003_randr.py     |  35 +++
 kpis/models.py                    |  19 +-
 kpis/views.py                     |  61 +++-
 templates/index.html              | 110 +++----
 templates/kpis/reports/randr.html | 583 ++++++++++++++++++++++++++++++++++++++
 5 files changed, 751 insertions(+), 57 deletions(-)

+ commit ac759fc6caeee3f7920ee67599d40477adf021d5
Author: Josh at Moms <josh@virtualraremedia.com>
- Date:   Mon Oct 23 12:43:48 2023 -0700

    test index.html GET feedback fix 1

 templates/index.html | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

+ commit f17d23f698937f2f42e98ee69cde1fd593cd5f14
Author: Josh at Moms <josh@virtualraremedia.com>
- Date:   Mon Oct 23 12:34:01 2023 -0700

    upated delta indicators beyond dummy data in monthly report

 expenseswebsite/static/js/modular_line.js |   1 +
 templates/kpis/monthly_report.html        | 213 ++++++++++++++++++++++++------
 2 files changed, 175 insertions(+), 39 deletions(-)

+ commit e70ae88094eafb6c8c35e333d3caae1c1c20fe01
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Sun Oct 22 15:10:18 2023 -0500

    minor 3

 expenseswebsite/static/js/piexample.js | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

+ commit e928b61a84d12e84045d3e585fa70e75b712dd46
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Sun Oct 22 15:08:32 2023 -0500

    minor 2

 templates/index.html | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

+ commit 2b60792d582e1f7965c9c99854f2f7ef6c3b01e9
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Sun Oct 22 15:06:39 2023 -0500

    minor 1

 expenseswebsite/static/js/piexample.js | 2 +-
 templates/index.html                   | 2 +-
 2 files changed, 2 insertions(+), 2 deletions(-)

+ commit 9271c9ac923e1597616ea4ca3360c013b50d72a0
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Sun Oct 22 15:00:32 2023 -0500

    formatting

 expenseswebsite/static/js/coffee.js    | 14 +++++++-------
 expenseswebsite/static/js/piexample.js | 11 ++++++++++-
 templates/index.html                   |  9 +++++++--
 3 files changed, 24 insertions(+), 10 deletions(-)

+ commit e95ab98965cd0729be60b8943e716eb46896b282
Author: Josh at Moms <josh@virtualraremedia.com>
- Date:   Sun Oct 22 11:16:59 2023 -0700

    minor

 expenseswebsite/static/js/coffee.js | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)

+ commit 97b191e41907d818fcc871ad973223f2761c6c82
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Sat Oct 21 02:59:51 2023 -0500

    playing with some new ideas

 expenseswebsite/static/js/coffee.js    | 47 +++++++++++++++++
 expenseswebsite/static/js/fancybar.js  | 95 ++++++++++++++++++++++++++++++++++
 expenseswebsite/static/js/piexample.js | 50 ++++++++++++++++++
 templates/index.html                   | 57 +++++++++++++++++---
 4 files changed, 243 insertions(+), 6 deletions(-)

+ commit feed66cae0c7895876dc1c5056fb3d57bae07c10
Author: Josh at Moms <josh@virtualraremedia.com>
- Date:   Fri Oct 20 18:07:14 2023 -0700

    added more metric tools to monthly reports

 expenseswebsite/static/js/modular_line.js |  90 ++++++++---
 expenseswebsite/static/js/sales_plotly.js |  17 ++
 kpis/views.py                             |  23 ++-
 templates/kpis/monthly_report.html        | 249 +++++++++++++++++++++++++++---
 4 files changed, 337 insertions(+), 42 deletions(-)

+ commit f7f2df41745ce80bcecc73d8e14607be4113a768
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Fri Oct 20 02:30:16 2023 -0500

    working on monthly comparisson line graph

 expenseswebsite/static/js/modular_line.js |  4 ----
 kpis/views.py                             | 26 +++++---------------------
 2 files changed, 5 insertions(+), 25 deletions(-)

+ commit ef06552462e3acf3dece52029416630bdcd1b9aa
Author: Josh at Moms <josh@virtualraremedia.com>
- Date:   Thu Oct 19 13:21:16 2023 -0700

    Changed the monthly report layout and worked on the modular graph

 expenseswebsite/static/js/modular_line.js | 131 ++++++++++++++++++++++++++++++
 kpis/urls.py                              |   1 +
 kpis/views.py                             |  44 +++++++++-
 templates/kpis/edit_sales.html            |  22 ++++-
 templates/kpis/monthly_report.html        |  60 ++++++++++----
 5 files changed, 236 insertions(+), 22 deletions(-)

+ commit f382a6f9895fa5d28d8642e1cc7906db7354ddc2
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Thu Oct 19 02:10:22 2023 -0500

    The monthly reports template is ready to be copied out to the different monthly reports pages

 kpis/views.py                  | 40 ++++++++++++++++++----------------------
 templates/kpis/edit_sales.html | 31 +++++++++++++++++++++++++++++++
 2 files changed, 49 insertions(+), 22 deletions(-)

+ commit 18484136881af4f12dd49d467956557a6fc2e9a7
Author: Josh at Moms <josh@virtualraremedia.com>
- Date:   Wed Oct 18 21:31:07 2023 -0700

    Sorted out some implementations towards monthly reports just about ready to copy and paste to future sections

 3                                 | 145 --------------------------------------
 kpis/urls.py                      |   1 +
 kpis/views.py                     |  60 +++++++++++-----
 templates/kpis/edit_sales.html    |  45 ++----------
 templates/kpis/modify_report.html |  72 ++++---------------
 5 files changed, 63 insertions(+), 260 deletions(-)

+ commit 1475af51cd5810185033c2bfaab0993b497113a8
Author: Josh at Moms <josh@virtualraremedia.com>
- Date:   Wed Oct 18 11:28:05 2023 -0700

    minor

 kpis/views.py | 11 ++++++++---
 1 file changed, 8 insertions(+), 3 deletions(-)

+ commit d95ca8a337d3d057ef702752c12ff08a4255e64c
Author: Josh at Moms <josh@virtualraremedia.com>
- Date:   Wed Oct 18 11:27:11 2023 -0700

    Changing the way you view and modify reports

 templates/kpis/edit_sales.html        | 107 ++++++++++++++++++++++-
 templates/kpis/edit_sales_backup.html | 158 ++++++++++++++++++++++++++++++++++
 templates/kpis/modify_report.html     | 158 ++++++++++++++++++++++++++++++++++
 3 files changed, 419 insertions(+), 4 deletions(-)

+ commit afb7be01c5c051be67a390279cb2248ec89c181a
Author: Josh at Moms <josh@virtualraremedia.com>
- Date:   Tue Oct 17 12:41:26 2023 -0700

    Fixes the search issues

 templates/expenses/index.html      | 14 +++++++-------
 templates/kpis/monthly_report.html |  2 +-
 2 files changed, 8 insertions(+), 8 deletions(-)

+ commit cdc5de831be2873b64f44fc2ce6632f1f64cedf6
Author: joshjetson <joshjetson@gmail.com>
- Date:   Sun Oct 15 20:50:40 2023 -0500

    changed table responsivness

 expenseswebsite/static/css/extra.css | 1 +
 templates/assets/index.html          | 2 +-
 templates/expenses/index.html        | 7 +++----
 templates/income/index.html          | 2 +-
 templates/liabs/index.html           | 2 +-
 5 files changed, 7 insertions(+), 7 deletions(-)

+ commit 3282648dcdcfd4c4295d710e9d5c93053461f7b3
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Sat Oct 14 11:24:38 2023 -0500

    Fixed some layout issues and added tables and carb bodies to the different financial sections

 expenseswebsite/static/js/searchAssets.js   |  2 +-
 expenseswebsite/static/js/searchExpenses.js |  2 +-
 expenseswebsite/static/js/searchIncome.js   |  2 +-
 expenseswebsite/static/js/searchLiabs.js    |  2 +-
 pdphases.md                                 |  8 +++++
 templates/assets/index.html                 | 45 +++++++++++++----------------
 templates/expenses/index.html               | 22 ++++++++------
 templates/income/index.html                 | 28 +++++++++---------
 templates/kpis/edit_sales.html              | 15 +++++++++-
 templates/liabs/index.html                  | 29 ++++++++-----------
 10 files changed, 84 insertions(+), 71 deletions(-)

+ commit 822029ea0a5173ca5649e35820c11835d7a7ebf2
Author: joshjetson <joshjetson@gmail.com>
- Date:   Fri Oct 13 15:21:41 2023 -0500

    minor changes

 templates/kpis/monthly_report.html | 5 +++--
 1 file changed, 3 insertions(+), 2 deletions(-)

+ commit 4d2243dc1cee5a5009135b08fd2bcc3d6770ab54
Author: joshjetson <joshjetson@gmail.com>
- Date:   Fri Oct 13 13:42:06 2023 -0500

    Changed some colors on the cards in reports

 expenseswebsite/static/css/extra.css | 77 ++++++++++++++++++++++++++++++++++++
 templates/kpis/monthly_report.html   | 27 ++++++++-----
 2 files changed, 95 insertions(+), 9 deletions(-)

+ commit dba3740d2288a335e0396a8706b3e87b0cbf90ae
Author: joshjetson <joshjetson@gmail.com>
- Date:   Fri Oct 13 12:17:49 2023 -0500

    added a new design to monthly report using cards for kpis

 expenseswebsite/static/css/extra.css | 192 +++++++++++++++++++++++++++++++++++
 templates/base.html                  |   1 +
 templates/kpis/monthly_report.html   | 120 +++++++++++++++++-----
 3 files changed, 287 insertions(+), 26 deletions(-)

+ commit d2a33668c1692011c646e006e80103958b9d7a95
Author: joshjetson <joshjetson@gmail.com>
- Date:   Wed Oct 11 21:55:28 2023 -0500

    added some of the formula data

 kpis/views.py                          |   9 +++++++--
 metrics/Monthly Report Input page.docx | Bin 13400 -> 13430 bytes
 metrics/monthly_report.md              |   1 +
 templates/kpis/monthly_report.html     |  11 ++++++-----
 4 files changed, 14 insertions(+), 7 deletions(-)

+ commit 3e680a668f7865aed3f78761ba99b2069747d1d5
Author: joshjetson <joshjetson@gmail.com>
- Date:   Wed Oct 11 20:18:50 2023 -0500

    Almost finished with the monthly report template so I can just copy and paste to make them all

 expenses/views.py              |  2 +-
 kpis/views.py                  | 52 +++++++++++++++++++++++++-----------------
 pdphases.md                    | 24 ++++++++++++++++++-
 templates/kpis/edit_sales.html | 26 ++++++++++++++++++++-
 4 files changed, 80 insertions(+), 24 deletions(-)

+ commit 97c7bca8ca2c41fca50d32f2dc7298b38fa91d04
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Tue Oct 10 15:24:03 2023 -0500

    Reports section is coming together. Worked out most of the logic and issues surrounding it

 expenses/models.py                    |  1 -
 expenses/views.py                     | 16 ++++--
 kpis/migrations/0001_initial.py       | 31 ++++++++++++
 kpis/migrations/0002_reports_owner.py | 22 ++++++++
 kpis/models.py                        | 18 +++++++
 kpis/views.py                         | 95 +++++++++++++++++++++++++++++++++--
 pdphases.md                           | 19 +++++++
 templates/kpis/edit_sales.html        | 58 +++++----------------
 templates/kpis/monthly_report.html    | 13 ++---
 9 files changed, 210 insertions(+), 63 deletions(-)

+ commit de2b83601f809fb47c5718f8e17c2edd391847c6
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Sat Oct 7 15:48:01 2023 -0500

    Shaping the reports sections

 expenseswebsite/static/css/bootstrap.css |     2 +-
 expenseswebsite/static/js/chart.js       | 11454 ++++++++++++++++++++++++++++-
 expenseswebsite/static/js/old_chart.js   |    10 +
 kpis/urls.py                             |     1 +
 kpis/views.py                            |    16 +-
 metrics/monthly_report.md                |   165 +
 pdphases.md                              |    24 +-
 templates/kpis/edit_sales.html           |   155 +
 templates/kpis/full_report.html          |   155 +
 templates/kpis/monthly_report.html       |   123 +-
 templates/kpis/sales_report.html         |   155 +
 11 files changed, 12176 insertions(+), 84 deletions(-)

+ commit 8fdb28d5ea064f1a46e0b7519c7018e24f8eda43
Author: joshjetson <joshjetson@gmail.com>
- Date:   Fri Oct 6 13:51:41 2023 -0500

    added phases notes

 screenshots/doughnut.png             | Bin 0 -> 171596 bytes
 screenshots/fullscreen.png           | Bin 0 -> 124136 bytes
 screenshots/menu_button.png          | Bin 0 -> 227600 bytes
 screenshots/mobile_cgraph.PNG        | Bin 0 -> 297587 bytes
 screenshots/mobile_graph.PNG         | Bin 0 -> 261899 bytes
 screenshots/mobile_landing.PNG       | Bin 0 -> 287566 bytes
 screenshots/mobile_monthly.PNG       | Bin 0 -> 212349 bytes
 screenshots/mobile_sidebar.PNG       | Bin 0 -> 236156 bytes
 screenshots/monthly_report_sales.png | Bin 0 -> 187024 bytes
 screenshots/side_bar.png             | Bin 0 -> 236260 bytes
 10 files changed, 0 insertions(+), 0 deletions(-)

+ commit 7a10eebe22b2fc396fcd2fbe903d23170d6025be
Author: joshjetson <joshjetson@gmail.com>
- Date:   Fri Oct 6 02:29:15 2023 -0500

    Some aesthetic changes and some updates to monthly_reports

 expenseswebsite/static/img/board_room.png      | Bin 0 -> 84547 bytes
 expenseswebsite/static/img/myvchart.png        | Bin 0 -> 782481 bytes
 expenseswebsite/static/img/vchart.jpg          | Bin 0 -> 1662226 bytes
 metrics/.~lock.Monthly Report Input page.docx# |   1 -
 pdphases.md                                    |  71 +++++++++++++++++++++++++
 templates/index.html                           |   8 ++-
 templates/kpis/monthly_report.html             |   4 +-
 7 files changed, 79 insertions(+), 5 deletions(-)

+ commit 6bf3870abf1b200e5a0731727ad3397e85b93bf8
Author: joshjetson <joshjetson@gmail.com>
- Date:   Thu Oct 5 20:27:23 2023 -0500

    Some changes to the monthly report page

 3                                              | 145 +++++++++++++++++
 metrics/.~lock.Monthly Report Input page.docx# |   2 +-
 metrics/Monthly Report Input page.docx         | Bin 23698 -> 13400 bytes
 templates/base.html                            |   2 +-
 templates/index.html                           |   3 +-
 templates/kpis/kpis_main.html                  |   3 +-
 templates/kpis/monthly_report.html             | 208 ++++++++++++++++---------
 trash.html                                     | 140 +++++++++++++++++
 8 files changed, 421 insertions(+), 82 deletions(-)

+ commit d65345e4d5082663700a006a70cca8bd3e25905b
Author: joshjetson <joshjetson@gmail.com>
- Date:   Thu Oct 5 13:18:16 2023 -0500

    Major aesthetic changes, major

 expenseswebsite/static/css/bootstrap.css | 12750 +++++++++++++++++++++++++++++
 templates/admin/base_site.html           |     2 +-
 templates/assets/add_asset.html          |     2 +-
 templates/assets/edit-asset.html         |     2 +-
 templates/assets/index.html              |    10 +-
 templates/base.html                      |    12 +-
 templates/base_auth.html                 |     4 +-
 templates/expenses/add_expense.html      |     2 +-
 templates/expenses/edit-expense.html     |     2 +-
 templates/expenses/index.html            |     4 +-
 templates/income/add_income.html         |     2 +-
 templates/income/edit_income.html        |     2 +-
 templates/income/inc_stats.html          |     9 +-
 templates/income/index.html              |     4 +-
 templates/index.html                     |    12 +-
 templates/kpis/kpis_main.html            |     8 +-
 templates/kpis/monthly_report.html       |     4 +-
 templates/liabs/add_liab.html            |     2 +-
 templates/liabs/edit-liab.html           |     2 +-
 templates/liabs/index.html               |     4 +-
 templates/partials/sidebar.html          |     4 +-
 21 files changed, 12796 insertions(+), 47 deletions(-)

+ commit e0c18f8b1fe424f5665777d582ebde6f62d385e1
Author: joshjetson <joshjetson@gmail.com>
- Date:   Wed Oct 4 18:37:27 2023 -0500

    reports page intiial

 expenseswebsite/static/css/paper.css | 35 +++++++++++++
 kpis/urls.py                         |  1 +
 kpis/views.py                        |  4 ++
 templates/base.html                  |  1 +
 templates/index.html                 | 43 +---------------
 templates/kpis/monthly_report.html   | 98 ++++++++++++++++++++++++++++++++++++
 templates/partials/sidebar.html      |  5 ++
 7 files changed, 146 insertions(+), 41 deletions(-)

+ commit 4974e13cd4e58874ba4a3b33c77920bd44e5f904
Author: joshjetson <joshjetson@gmail.com>
- Date:   Wed Oct 4 14:13:00 2023 -0500

    Fixes some of the layout

 expenseswebsite/static/css/dashboard.css | 10 ++++
 templates/base.html                      | 40 ++++++--------
 templates/index.html                     | 95 ++++++++++++++++++++++----------
 templates/partials/sidebar.html          |  9 ++-
 4 files changed, 102 insertions(+), 52 deletions(-)

+ commit 178eaeaa114d778ce2d102246c8140318715e025
Author: joshjetson <joshjetson@gmail.com>
- Date:   Wed Oct 4 00:54:08 2023 -0500

    Made some major changes. Added a greetings page and a whole bunch of other things. Check the difs with lazygit

 authentication/views.py                |   2 +-
 expenseswebsite/static/css/product.css |  81 +++++++++++++
 kpis/views.py                          |   1 -
 templates/base.html                    |  49 ++++++--
 templates/index.html                   | 209 +++++++++++++++++++++++++++++++++
 templates/partials/sidebar.html        |  13 +-
 userpreferences/urls.py                |   3 +-
 userpreferences/views.py               |   4 +
 8 files changed, 349 insertions(+), 13 deletions(-)

+ commit 2aea3fcecba943f298c40de74c6c812b396cd1f2
Author: joshjetson <joshjetson@gmail.com>
- Date:   Tue Oct 3 15:36:01 2023 -0500

    Did some refactoring in order to make the javascript responsible for the search reusable, also cleaned up the html inside the sidebar.html making the sidebar look cleaner. Got rid of the toggling Accounting section and just keeping it static for consistency and it looks cleaner

 expenseswebsite/static/js/searchAssets.js      |   8 +-
 metrics/.~lock.Monthly Report Input page.docx# |   1 +
 pdphases.md                                    | 113 +++++++++++++++++++++++++
 templates/assets/index.html                    |   2 +-
 templates/partials/sidebar.html                |  82 +++++++-----------
 5 files changed, 152 insertions(+), 54 deletions(-)

+ commit 93f64bab9719829c90236b5251ece01e771ab37b
Author: joshjetson <joshjetson@gmail.com>
- Date:   Mon Oct 2 16:00:52 2023 -0500

    updated the menu

 templates/partials/sidebar.html | 41 +++++++++++++++++++++++++----------------
 1 file changed, 25 insertions(+), 16 deletions(-)

+ commit 0e9869b36a5497615abf70b97f1365dc9710d4c9
Author: joshjetson <joshjetson@gmail.com>
- Date:   Mon Oct 2 15:09:27 2023 -0500

    Fixed the searches in accounting respective towards each financial you can now search, find an entry and then edit the entry found directly through the search

 expenseswebsite/static/js/searchAssets.js   | 7 ++++---
 expenseswebsite/static/js/searchExpenses.js | 3 ++-
 expenseswebsite/static/js/searchIncome.js   | 3 ++-
 expenseswebsite/static/js/searchLiabs.js    | 3 ++-
 templates/assets/index.html                 | 4 ++--
 templates/expenses/index.html               | 2 +-
 templates/income/index.html                 | 2 +-
 templates/liabs/index.html                  | 2 +-
 8 files changed, 15 insertions(+), 11 deletions(-)

+ commit 339d230fd6f5b23f7e65919d7c4e27ca24837b9a
Author: joshjetson <joshjetson@gmail.com>
- Date:   Mon Oct 2 11:00:35 2023 -0500

    Changed the layout for financial pages

 expenseswebsite/static/css/bootstrap.min.css |  6 ++--
 templates/assets/index.html                  | 48 ++++++++++++++++++----------
 templates/expenses/index.html                | 40 +++++++++++++----------
 templates/income/inc_stats.html              |  8 +++--
 templates/income/index.html                  | 40 +++++++++++++----------
 templates/liabs/index.html                   | 39 ++++++++++++----------
 6 files changed, 107 insertions(+), 74 deletions(-)

+ commit 7ccb65b93fba388334dc131c89e37f0c116f65a0
Author: joshjetson <joshjetson@gmail.com>
- Date:   Mon Oct 2 00:56:15 2023 -0500

    Updated the charts to the current version which repaired the 404 devtools error in the console

 templates/expenses/expense_bar.html  | 2 +-
 templates/expenses/expense_line.html | 2 +-
 templates/expenses/stats.html        | 2 +-
 templates/income/inc_bar.html        | 2 +-
 templates/income/inc_doughnut.html   | 2 +-
 templates/income/inc_stats.html      | 2 +-
 templates/kpis/kpis_main.html        | 2 +-
 7 files changed, 7 insertions(+), 7 deletions(-)

+ commit 820f4a7ac922430fcf082fcdd40ca1f00b2fa299
Author: joshjetson <joshjetson@gmail.com>
- Date:   Mon Oct 2 00:28:31 2023 -0500

    Made some modifications towards mobile enviornments

 templates/partials/sidebar.html | 12 ++++--------
 1 file changed, 4 insertions(+), 8 deletions(-)

+ commit a905d578723a575ce4e11372e0df9cdadbe7ff92
Author: joshjetson <joshjetson@gmail.com>
- Date:   Sun Oct 1 23:56:35 2023 -0500

    changed the sidebar to hidden activated with a button and added the usecolor css class which im using to change different sections font and color

 "\\"                                         |  57 ------
 authentication/views.py                      |   6 +-
 expenseswebsite/static/css/bootstrap.min.css |   2 +-
 expenseswebsite/static/css/dashboard.css     |  36 +++-
 metrics/Monthly Report Input page.docx       | Bin 0 -> 23698 bytes
 templates/REBASE.html                        | 251 +++++++++++++++++++++++++++
 templates/assets/add_asset.html              |   2 +-
 templates/assets/edit-asset.html             |   2 +-
 templates/assets/index.html                  |  12 +-
 templates/base.html                          |   9 +-
 templates/expenses/add_expense.html          |   2 +-
 templates/expenses/edit-expense.html         |   2 +-
 templates/expenses/index.html                |   2 +-
 templates/income/add_income.html             |   2 +-
 templates/income/edit_income.html            |   2 +-
 templates/income/index.html                  |   2 +-
 templates/kpis/kpis_main.html                |   6 +-
 templates/liabs/add_liab.html                |   2 +-
 templates/liabs/edit-liab.html               |   2 +-
 templates/liabs/index.html                   |   2 +-
 templates/partials/sidebar.html              | 160 +++++++++--------
 templates/partials/tesbar.html               |  51 +++---
 22 files changed, 421 insertions(+), 191 deletions(-)

+ commit 0db8b7dddce74659146c7959430832b93dffe56e
Author: joshjetson <joshjetson@gmail.com>
- Date:   Fri Sep 29 12:46:15 2023 -0500

    fixed division by zero error in KPIs if there is no user data for a financial category

 kpis/views.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

+ commit de3260b67e24b1d43d2f26eda9d89f6eb8ce8218
Author: joshjetson <joshjetson@gmail.com>
- Date:   Thu Sep 28 01:29:53 2023 -0500

    Sorted out major issues and got kpis in prelim stage

 "\\"                                  |  57 +++++++++++++++
 expenseswebsite/static/js/kpi_line.js | 131 ++++++++++++++++++++++++++++++++++
 kpis/urls.py                          |   2 +
 kpis/views.py                         |  92 ++++++++++++++++++------
 templates/kpis/kpis_main.html         |  49 +++++++++++--
 5 files changed, 305 insertions(+), 26 deletions(-)

+ commit 57c05361b291c1443d4780928367822e8148a436
Author: joshjetson <joshjetson@gmail.com>
- Date:   Mon Sep 25 14:19:21 2023 -0500

    fixed silly breadcrumb label

 templates/expenses/expense_bar.html  | 2 +-
 templates/expenses/expense_line.html | 2 +-
 templates/expenses/stats.html        | 2 +-
 3 files changed, 3 insertions(+), 3 deletions(-)

+ commit adede60408766e5c84b81cae11384a89ae0e63d4
Author: joshjetson <joshjetson@gmail.com>
- Date:   Mon Sep 25 14:10:49 2023 -0500

    Routed everything for Liabilites

 assets/urls.py                                     |   2 +
 assets/views.py                                    |  32 -----
 expenses/apps.py                                   |   1 +
 ..._category_id_alter_category_type_id_and_more.py |  33 +++++
 expenseswebsite/settings.py                        |   1 +
 expenseswebsite/static/js/searchAssets.js          |  50 ++++++++
 expenseswebsite/static/js/searchExpenses.js        |   3 +-
 expenseswebsite/static/js/searchIncome.js          |   1 +
 expenseswebsite/static/js/searchLiabs.js           |  50 ++++++++
 expenseswebsite/urls.py                            |   1 +
 templates/assets/index.html                        |   2 +-
 templates/liabs/add_liab.html                      |  73 +++++++++++
 templates/liabs/edit-liab.html                     |  96 ++++++++++++++
 templates/liabs/index.html                         | 140 +++++++++++++++++++++
 templates/partials/tesbar.html                     |   2 +-
 userincome/apps.py                                 |   1 +
 ...lter_source_id_alter_source_type_id_and_more.py |  33 +++++
 17 files changed, 486 insertions(+), 35 deletions(-)

+ commit 074f850bcb6d19bd7fe3f8986e3a7aab5b6f9af7
Author: joshjetson <joshjetson@gmail.com>
- Date:   Mon Sep 25 14:10:25 2023 -0500

    Routed everything for Liabilites

 liabs/__init__.py                |   0
 liabs/admin.py                   |  17 +++++
 liabs/apps.py                    |   6 ++
 liabs/migrations/0001_initial.py |  82 +++++++++++++++++++++
 liabs/migrations/__init__.py     |   0
 liabs/models.py                  |  34 +++++++++
 liabs/tests.py                   |   3 +
 liabs/urls.py                    |  12 +++
 liabs/views.py                   | 154 +++++++++++++++++++++++++++++++++++++++
 9 files changed, 308 insertions(+)

+ commit f97b7ddba808955d044f7e28e75d2bef25402d5e
Author: joshjetson <joshjetson@gmail.com>
- Date:   Mon Sep 25 12:34:19 2023 -0500

    Assets section done, Expense and Income chart functionality fine, sorted out dynamic chart generation passing values to the js from the <script> tags in the html

 assets/__init__.py                   |   0
 assets/admin.py                      |  17 ++++
 assets/apps.py                       |   6 ++
 assets/migrations/0001_initial.py    |  82 +++++++++++++++
 assets/migrations/__init__.py        |   0
 assets/models.py                     |  34 +++++++
 assets/tests.py                      |   3 +
 assets/urls.py                       |  10 ++
 assets/views.py                      | 186 +++++++++++++++++++++++++++++++++++
 expenses/urls.py                     |   2 +
 expenses/views.py                    |   3 +
 expenseswebsite/settings.py          |   1 +
 expenseswebsite/static/js/stats.js   |  10 +-
 expenseswebsite/urls.py              |   1 +
 templates/assets/add_asset.html      |  73 ++++++++++++++
 templates/assets/edit-asset.html     |  96 ++++++++++++++++++
 templates/assets/index.html          | 140 ++++++++++++++++++++++++++
 templates/expenses/expense_bar.html  |  63 ++++++++++++
 templates/expenses/expense_line.html |   2 +-
 templates/expenses/stats.html        |   4 +-
 templates/partials/tesbar.html       |   2 +-
 21 files changed, 726 insertions(+), 9 deletions(-)

+ commit 8872baf29341338905b277a35b62e7edfafac938
Author: joshjetson <joshjetson@gmail.com>
- Date:   Sun Sep 24 15:44:05 2023 -0500

    Fixed some site navigation issues, this is pre assets and liabilites apps

 expenseswebsite/static/js/exp_stats.js             |  2 +-
 expenseswebsite/static/js/inc_stats.js             |  3 --
 expenseswebsite/static/js/stats.js                 |  4 +--
 expenseswebsite/urls.py                            |  4 +--
 templates/expenses/expense_line.html               | 21 ++++++++-----
 templates/expenses/stats.html                      | 17 +++++++---
 templates/income/add_income.html                   | 10 ++++++
 templates/income/edit_income.html                  | 14 +++++++++
 templates/income/inc_bar.html                      |  6 ++++
 templates/income/inc_doughnut.html                 |  6 ++++
 templates/income/inc_stats.html                    |  8 +++--
 templates/income/index.html                        |  3 ++
 templates/kpis/kpis_main.html                      |  7 +++--
 templates/partials/tesbar.html                     | 16 +++++-----
 trash.html                                         |  0
 userincome/admin.py                                |  3 +-
 .../0003_source_type_userincome_source_type.py     | 36 ++++++++++++++++++++++
 userincome/models.py                               |  9 ++++++
 userincome/views.py                                | 20 +++++++++---
 19 files changed, 148 insertions(+), 41 deletions(-)

+ commit 843f4baed94b8cb3175f1c81189e84661187952b
Author: joshjetson <joshjetson@gmail.com>
- Date:   Sat Sep 23 23:54:29 2023 -0500

    sorted out all of the new category type routes for each view, models and template pages

 expenses/views.py                    |  2 ++
 templates/expenses/edit-expense.html | 14 ++++++++++++++
 templates/expenses/index.html        |  2 ++
 3 files changed, 18 insertions(+)

+ commit 213ad32f5b37415684688836c62f751f43a58763
Author: joshjetson <joshjetson@gmail.com>
- Date:   Sat Sep 23 22:28:54 2023 -0500

    added a category type in the expenses section

 expenses/admin.py                                  | 10 +++---
 .../0004_category_type_expense_category_type.py    | 36 ++++++++++++++++++++++
 expenses/models.py                                 | 11 ++++++-
 expenses/views.py                                  | 19 +++++++++---
 templates/expenses/add_expense.html                | 16 +++++++---
 5 files changed, 78 insertions(+), 14 deletions(-)

+ commit 4cb60a91e254eb5e00b973ae9cb51a938c3dc2f5
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Sat Sep 23 09:59:44 2023 -0500

    added some stuff to the kpis views

 kpis/views.py                    | 34 ++++++++++++++++++++++++++++++++++
 mermaid_diagrams.md              |  5 +++++
 metrics.csv                      |  1 +
 templates/partials/_sidebar.html |  1 +
 4 files changed, 41 insertions(+)

+ commit eb291547695ac9989a5f0c55e1efd4706c97d664
Author: joshjetson <joshjetson@gmail.com>
- Date:   Fri Sep 22 23:17:39 2023 -0500

    sorted out .env file for safety reasons

 expenseswebsite/.env           |  2 ++
 expenseswebsite/settings.py    | 10 +++-------
 templates/partials/tesbar.html | 24 ++++++++++++------------
 3 files changed, 17 insertions(+), 19 deletions(-)

+ commit 5e41ea0716ac63e60d8c318ce31d93f22c3349fb
Author: joshjetson <joshjetson@gmail.com>
- Date:   Fri Sep 22 13:12:00 2023 -0500

    not noteworthy change

 expenseswebsite/static/js/inc_stats.js | 1 -
 1 file changed, 1 deletion(-)

+ commit c130472702e2e230bbb9d2bebd48df58774f9e25
Author: joshjetson <joshjetson@gmail.com>
- Date:   Fri Sep 22 13:08:00 2023 -0500

    added Accounting dropdown menu and assets and liabilities navbar links that dont work yet

 expenseswebsite/static/css/dashboard.css  |  11 ++
 expenseswebsite/static/img/favicon.png    | Bin 0 -> 132418 bytes
 expenseswebsite/static/js/inc_doughnut.js |  10 +-
 expenseswebsite/static/js/inc_stats.js    |   5 +-
 metrics/formulas_and_visualizations.md    |  60 ++++++++++
 templates/admin/base_site.html            |   2 +-
 templates/base.html                       |   3 +-
 templates/income/inc_doughnut.html        |   4 +-
 templates/partials/sidebar.html           |   7 +-
 templates/partials/tesbar.html            | 192 ++++++++++++++++--------------
 10 files changed, 190 insertions(+), 104 deletions(-)

+ commit b0f05fd58922a3c91eb0773947e52ad189c334b0
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Fri Sep 15 21:47:17 2023 -0500

    added links from login to registration and vice versa

 templates/authentication/login.html    | 1 +
 templates/authentication/register.html | 1 +
 2 files changed, 2 insertions(+)

+ commit 165821bad91db22e67d476b9754f5f34eb0535c1
Author: joshjetson <joshjetson@gmail.com>
- Date:   Fri Sep 15 15:18:20 2023 -0500

    updated steps.md

 steps.md | 17 +++++++++++------
 1 file changed, 11 insertions(+), 6 deletions(-)

+ commit fbcb5f1e263f6a7e0066f762ba2e2e1b44eb40bf
Author: Josh <josh@virtualraremedia.com>
- Date:   Fri Sep 15 15:14:16 2023 -0500

    updating the settings file from the production server to include the hosts static ip and registered domain name

 expenseswebsite/settings.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

+ commit 2eef43df3041b92f183f7fca4ac1fa43fb7349a3
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Thu Sep 14 18:40:48 2023 -0500

    added the kpis app_1

 templates/kpis/{kpi_main.html => kpis_main.html} | 0
 1 file changed, 0 insertions(+), 0 deletions(-)

+ commit c2fc04bcae4727dfd97c8a5c32bd5bc18d73e9fb
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Thu Sep 14 18:35:44 2023 -0500

    added the kpis app

 expenses/urls.py               |  1 -
 expenses/views.py              |  2 ++
 expenseswebsite/settings.py    |  1 +
 expenseswebsite/urls.py        |  1 +
 kpis/__init__.py               |  0
 kpis/admin.py                  |  3 +++
 kpis/apps.py                   |  6 +++++
 kpis/migrations/__init__.py    |  0
 kpis/models.py                 |  3 +++
 kpis/tests.py                  |  3 +++
 kpis/urls.py                   |  6 +++++
 kpis/views.py                  | 14 +++++++++++
 templates/admin/base_site.html |  2 +-
 templates/base.html            | 14 ++++++-----
 templates/base_auth.html       | 12 ++++-----
 templates/kpis/kpi_main.html   | 56 ++++++++++++++++++++++++++++++++++++++++++
 userincome/views.py            |  3 +++
 userpreferences/views.py       |  2 ++
 18 files changed, 115 insertions(+), 14 deletions(-)

+ commit e08a8ad29e9496cf7bf1207ccd27cff67d274f5b
Author: joshjetson <joshjetson@gmail.com>
- Date:   Thu Sep 14 01:11:18 2023 -0500

    more chart functionality

 expenses/urls.py                       |  6 +++-
 expenses/views.py                      | 24 ++++++++++++++
 expenseswebsite/static/js/exp_stats.js | 60 ++++++++++++++++++++++++++++++++++
 expenseswebsite/static/js/inc_bar.js   | 56 +++++++++++++++++++++++++++++++
 templates/base.html                    | 10 ++----
 templates/expenses/expense_line.html   | 56 +++++++++++++++++++++++++++++++
 templates/expenses/stats.html          |  4 +--
 templates/income/inc_bar.html          | 56 +++++++++++++++++++++++++++++++
 templates/income/inc_doughnut.html     |  4 +--
 templates/income/inc_stats.html        |  4 +--
 templates/partials/_sidebar.html       |  1 +
 userincome/urls.py                     |  2 ++
 userincome/views.py                    |  5 ++-
 13 files changed, 271 insertions(+), 17 deletions(-)

+ commit c12608c13ece4691ba5ef45ef4ad00e135f17448
Author: joshjetson <joshjetson@gmail.com>
- Date:   Wed Sep 13 22:51:33 2023 -0500

    added tabs

 expenseswebsite/static/js/inc_doughnut.js | 56 +++++++++++++++++++++++++++++++
 expenseswebsite/static/js/stats.js        |  3 +-
 mermaid_diagrams.md                       |  3 +-
 templates/base.html                       |  4 +--
 templates/expenses/stats.html             | 17 +++++++++-
 templates/income/inc_doughnut.html        | 56 +++++++++++++++++++++++++++++++
 templates/income/inc_stats.html           | 15 +++++++++
 templates/partials/_sidebar.html          | 17 ++++++++--
 userincome/urls.py                        |  6 +++-
 userincome/views.py                       | 31 ++++++++++++++---
 10 files changed, 194 insertions(+), 14 deletions(-)

+ commit beba61dcea569b4619c31fb5bba01c0dce722497
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Wed Sep 13 00:11:57 2023 -0500

    First + commit in dev branch

 mermaid_diagrams.md | 14 ++++++++++++++
 notes.md            |  2 +-
 steps.md            |  9 +++++----
 3 files changed, 20 insertions(+), 5 deletions(-)

+ commit 71d6e7ed6780100f2917f7e914d51f2716aa4d6b
Author: joshjetson <joshjetson@gmail.com>
- Date:   Tue Sep 12 21:52:22 2023 -0500

    added some stff to the .gitignore

 .gitignore | 19 ++++++++++++++++++-
 1 file changed, 18 insertions(+), 1 deletion(-)

+ commit d9340625d940778f248ee71bd2027000446d9485
Author: joshjetson <joshjetson@gmail.com>
- Date:   Tue Sep 12 21:43:37 2023 -0500

    Fixed the date sorting problem with the line graph

 expenseswebsite/static/js/inc_backup_stats.js | 59 +++++++++++++++++++++++++++
 expenseswebsite/static/js/inc_stats.js        |  5 ++-
 userincome/views.py                           | 30 +++++++++-----
 3 files changed, 81 insertions(+), 13 deletions(-)

+ commit 1d370eee034e0cdc66ad53c58cf4959886e1b6b0
Author: joshjetson <joshjetson@gmail.com>
- Date:   Tue Sep 12 12:21:00 2023 -0500

    worked out expenses and income display charts

 expenses/migrations/0003_alter_expense_options.py  |  16 ++
 expenses/models.py                                 |   3 +
 expenseswebsite/settings.py                        |   2 +-
 expenseswebsite/static/js/inc_stats.js             |  59 +++++
 expenseswebsite/static/js/stats.js                 |   5 +-
 notes.md                                           | 273 +++++++++++++++++++++
 steps.md                                           |   9 +-
 templates/base.html                                |   4 +-
 templates/income/inc_stats.html                    |  41 ++++
 templates/partials/_sidebar.html                   |   3 +-
 templates/partials/sidebar.html                    |   1 +
 .../migrations/0002_alter_userincome_options.py    |  16 ++
 userincome/urls.py                                 |   6 +-
 userincome/views.py                                |  28 +++
 14 files changed, 456 insertions(+), 10 deletions(-)

+ commit 8d22d07ecc5875cca5e7a0d5883eb462b3ec045c
Author: joshjetson <joshjetson@gmail.com>
- Date:   Sun Sep 10 22:58:25 2023 -0500

    added corse headers to requirments text

 requirements.txt | 1 +
 1 file changed, 1 insertion(+)

+ commit 64f173689ec06c4a8575e8526a4a1b0db1a28ae3
Author: joshjetson <joshjetson@gmail.com>
- Date:   Sun Sep 10 22:36:48 2023 -0500

    fixed alot of errors

 expenseswebsite/settings.py              | 10 +++-
 expenseswebsite/static/css/dashboard.css | 15 +++++-
 expenseswebsite/static/css/sidebaro.css  | 16 ++++++
 expenseswebsite/static/js/stats.js       |  2 +-
 templates/base.html                      | 27 +++++-----
 templates/expenses/stats.html            |  2 +-
 templates/partials/_sidebar.html         |  1 +
 templates/partials/sidebar.html          | 87 ++++++++++++++++++++++++++++++
 templates/partials/sidebaro.css          | 16 ++++++
 templates/partials/tesbar.html           | 93 ++++++++++++++++++++++++++++++++
 templates/testbase.html                  | 93 ++++++++++++++++++++++++++++++++
 11 files changed, 343 insertions(+), 19 deletions(-)

+ commit 9a4de42d1fdfb0504881bc1b03bf4ebf720669d4
Author: joshjetson <joshjetson@gmail.com>
- Date:   Sat Sep 9 22:13:08 2023 -0500

    updated gitignore again

 .gitignore | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

+ commit 6dab465fea56ec2bbb0f1597ad973bc3cb1b2206
Author: joshjetson <joshjetson@gmail.com>
- Date:   Sat Sep 9 22:06:05 2023 -0500

    without the venv and updated the gitignore

 .gitignore                    |   1 +
 venv/bin/Activate.ps1         | 247 ------------------------------------------
 venv/bin/activate             |  69 ------------
 venv/bin/activate.csh         |  26 -----
 venv/bin/activate.fish        |  69 ------------
 venv/bin/django-admin         |   8 --
 venv/bin/gunicorn             |   8 --
 venv/bin/ipython              |   8 --
 venv/bin/ipython3             |   8 --
 venv/bin/pip                  |   8 --
 venv/bin/pip3                 |   8 --
 venv/bin/pip3.11              |   8 --
 venv/bin/pygmentize           |   8 --
 venv/bin/python               |   1 -
 venv/bin/python3              |   1 -
 venv/bin/python3.11           |   1 -
 venv/bin/sqlformat            |   8 --
 venv/lib64                    |   1 -
 venv/pyvenv.cfg               |   5 -
 venv/share/man/man1/ipython.1 |  60 ----------
 20 files changed, 1 insertion(+), 552 deletions(-)

+ commit 82ba0f3c2b5bd5cf6bc182038a1e84eda766a572
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Sat Sep 9 21:52:18 2023 -0500

    sorted out the charts.js issue

 expenseswebsite/static/js/stats.js |  2 +-
 package.json                       | 17 +++++++++++++++++
 templates/base.html                |  2 +-
 templates/expenses/stats.html      |  4 ++--
 venv/bin/activate                  |  2 +-
 venv/bin/activate.csh              |  2 +-
 venv/bin/activate.fish             |  2 +-
 venv/bin/django-admin              |  2 +-
 venv/bin/gunicorn                  |  2 +-
 venv/bin/ipython                   |  2 +-
 venv/bin/ipython3                  |  2 +-
 venv/bin/pip                       |  2 +-
 venv/bin/pip3                      |  2 +-
 venv/bin/pip3.11                   |  2 +-
 venv/bin/pygmentize                |  2 +-
 venv/bin/python                    |  2 +-
 venv/bin/python3                   |  2 +-
 venv/bin/python3.11                |  2 +-
 venv/bin/sqlformat                 |  2 +-
 venv/pyvenv.cfg                    |  2 +-
 20 files changed, 37 insertions(+), 20 deletions(-)

+ commit 65b8ce3900f5efaf5bdfd0380186063065e09bf4
Author: joshjetson <joshjetson@gmail.com>
- Date:   Fri Sep 8 16:56:28 2023 -0500

    updated the gitignore

 .gitignore       | 2 ++
 requirements.txt | 1 +
 2 files changed, 3 insertions(+)

+ commit 20997c3a62fe8cb53f6c7e76d42af0de79e42bf1
Author: joshjetson <joshjetson@gmail.com>
- Date:   Fri Sep 8 01:33:30 2023 -0500

    updated class meta in views got rid of many 404 errors

 expenses/models.py       |  2 +-
 steps.md                 |  9 ++++++++-
 templates/base.html      | 10 +++-------
 templates/base_auth.html |  6 +++---
 userincome/models.py     |  2 +-
 venv/bin/activate        |  2 +-
 venv/bin/activate.csh    |  2 +-
 venv/bin/activate.fish   |  2 +-
 venv/bin/django-admin    |  2 +-
 venv/bin/gunicorn        |  2 +-
 venv/bin/ipython         |  2 +-
 venv/bin/ipython3        |  2 +-
 venv/bin/pip             |  2 +-
 venv/bin/pip3            |  2 +-
 venv/bin/pip3.11         |  2 +-
 venv/bin/pygmentize      |  2 +-
 venv/bin/sqlformat       |  2 +-
 venv/pyvenv.cfg          |  2 +-
 18 files changed, 29 insertions(+), 26 deletions(-)

+ commit 90d539c2246562926268f4c4db6af3cca56a9e3a
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Thu Sep 7 14:09:11 2023 -0500

    added to steps

 steps.md | 10 ++++++++++
 1 file changed, 10 insertions(+)

+ commit 667f09416e0111dbb6bdb77da86894a681f5d194
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Wed Sep 6 20:39:04 2023 -0500

    added to steps

 steps.md | 1 +
 1 file changed, 1 insertion(+)

+ commit 7219c7978938dcc880109b98ab43ee1087662fba
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Wed Sep 6 20:28:16 2023 -0500

    got everything working

 expenses/views.py   | 5 ++++-
 userincome/views.py | 6 +++++-
 2 files changed, 9 insertions(+), 2 deletions(-)

+ commit 24f3eabc23be105bfd87fd5f8d134b392d7f68ca
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Wed Sep 6 15:45:21 2023 -0500

    almost there

 authentication/views.py       |  2 +-
 expenseswebsite/settings.py   |  6 ++---
 venv/bin/ipython              |  8 ++++++
 venv/bin/ipython3             |  8 ++++++
 venv/bin/pygmentize           |  8 ++++++
 venv/share/man/man1/ipython.1 | 60 +++++++++++++++++++++++++++++++++++++++++++
 6 files changed, 88 insertions(+), 4 deletions(-)

+ commit 1c6dc6871b0ccafd6b75e5cf569b49fc27b37889
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Wed Sep 6 00:27:24 2023 -0500

    some small upates more

 expenseswebsite/settings.py | 10 +++++-----
 1 file changed, 5 insertions(+), 5 deletions(-)

+ commit 06a18e0dd04bef287be36fa639a7b494001342b0
Author: Josh@codebro <joshjetson@gmail.com>
- Date:   Tue Sep 5 23:24:03 2023 -0500

    some small upates

 expenseswebsite/settings.py |  4 +++-
 steps.md                    | 21 +++++++++++++++++++++
 venv/bin/activate           |  2 +-
 venv/bin/activate.csh       |  2 +-
 venv/bin/activate.fish      |  2 +-
 venv/bin/django-admin       |  2 +-
 venv/bin/gunicorn           |  2 +-
 venv/bin/pip                |  2 +-
 venv/bin/pip3               |  2 +-
 venv/bin/pip3.11            |  2 +-
 venv/bin/sqlformat          |  2 +-
 venv/pyvenv.cfg             |  2 +-
 12 files changed, 34 insertions(+), 11 deletions(-)

+ commit 06904e0cb643c1f4bbce952416214dfc498befd6
Author: joshjetson <joshjetson@gmail.com>
- Date:   Tue Sep 5 19:16:03 2023 -0500

    Initial + commit from this machine

 .DS_Store                                      |   Bin 0 -> 6148 bytes
 .env-example                                   |     4 +
 .gitignore                                     |   109 +
 Pipfile                                        |    17 +
 Pipfile.lock                                   |   131 +
 Procfile                                       |     2 +
 authentication/__init__.py                     |     0
 authentication/admin.py                        |     3 +
 authentication/apps.py                         |     5 +
 authentication/migrations/__init__.py          |     0
 authentication/models.py                       |     3 +
 authentication/tests.py                        |     3 +
 authentication/urls.py                         |    16 +
 authentication/utils.py                        |    11 +
 authentication/views.py                        |   158 +
 currencies.json                                |   172 +
 db.sqlite3                                     |     0
 expenses/__init__.py                           |     0
 expenses/admin.py                              |    14 +
 expenses/apps.py                               |     5 +
 expenses/migrations/0001_initial.py            |    36 +
 expenses/migrations/0002_auto_20200508_1810.py |    17 +
 expenses/migrations/__init__.py                |     0
 expenses/models.py                             |    29 +
 expenses/tests.py                              |     3 +
 expenses/urls.py                               |    17 +
 expenses/views.py                              |   144 +
 expenseswebsite/.env                           |     4 +
 expenseswebsite/__init__.py                    |     0
 expenseswebsite/asgi.py                        |    16 +
 expenseswebsite/settings.py                    |   149 +
 expenseswebsite/static/css/adminstyle.css      |    30 +
 expenseswebsite/static/css/bootstrap.min.css   | 12148 +++++++++++++++++++++++
 expenseswebsite/static/css/dashboard.css       |   106 +
 expenseswebsite/static/css/main.css            |    23 +
 expenseswebsite/static/img/logo.png            |   Bin 0 -> 4955 bytes
 expenseswebsite/static/js/chart.js             |    10 +
 expenseswebsite/static/js/expensecharts.js     |    72 +
 expenseswebsite/static/js/getCategoryData.js   |     0
 expenseswebsite/static/js/main.js              |     1 +
 expenseswebsite/static/js/register.js          |    75 +
 expenseswebsite/static/js/searchExpenses.js    |    49 +
 expenseswebsite/static/js/searchIncome.js      |    47 +
 expenseswebsite/static/js/stats.js             |    56 +
 expenseswebsite/static/js/userStats.js         |   106 +
 expenseswebsite/urls.py                        |    25 +
 expenseswebsite/wsgi.py                        |    16 +
 manage.py                                      |    21 +
 requirements.txt                               |     6 +
 templates/admin/base_site.html                 |    12 +
 templates/admin/login.html                     |     6 +
 templates/authentication/activate_account.html |     3 +
 templates/authentication/login.html            |    53 +
 templates/authentication/register.html         |    71 +
 templates/authentication/reset-password.html   |    24 +
 templates/authentication/set-newpassword.html  |    24 +
 templates/base.html                            |    73 +
 templates/base_auth.html                       |    34 +
 templates/expenses/add_expense.html            |    65 +
 templates/expenses/edit-expense.html           |    83 +
 templates/expenses/index.html                  |   130 +
 templates/expenses/stats.html                  |    41 +
 templates/income/add_income.html               |    64 +
 templates/income/edit_income.html              |    83 +
 templates/income/index.html                    |   137 +
 templates/index.html                           |     0
 templates/partials/_messages.html              |     9 +
 templates/partials/_sidebar.html               |    75 +
 templates/preferences/index.html               |    31 +
 userincome/__init__.py                         |     0
 userincome/admin.py                            |     6 +
 userincome/apps.py                             |     5 +
 userincome/migrations/0001_initial.py          |    36 +
 userincome/migrations/__init__.py              |     0
 userincome/models.py                           |    26 +
 userincome/tests.py                            |     3 +
 userincome/urls.py                             |    13 +
 userincome/views.py                            |   110 +
 userpreferences/__init__.py                    |     0
 userpreferences/admin.py                       |     3 +
 userpreferences/apps.py                        |     5 +
 userpreferences/migrations/0001_initial.py     |    25 +
 userpreferences/migrations/__init__.py         |     0
 userpreferences/models.py                      |    11 +
 userpreferences/tests.py                       |     3 +
 userpreferences/urls.py                        |     6 +
 userpreferences/views.py                       |    36 +
 venv/bin/Activate.ps1                          |   247 +
 venv/bin/activate                              |    69 +
 venv/bin/activate.csh                          |    26 +
 venv/bin/activate.fish                         |    69 +
 venv/bin/django-admin                          |     8 +
 venv/bin/gunicorn                              |     8 +
 venv/bin/pip                                   |     8 +
 venv/bin/pip3                                  |     8 +
 venv/bin/pip3.11                               |     8 +
 venv/bin/python                                |     1 +
 venv/bin/python3                               |     1 +
 venv/bin/python3.11                            |     1 +
 venv/bin/sqlformat                             |     8 +
 venv/lib64                                     |     1 +
 venv/pyvenv.cfg                                |     5 +
 102 files changed, 15633 insertions(+)

 ```

 </details>
