odoo.define('sale_customize.lfm_widget_one2many', function (require) {
    "use strict";
    var fieldRegistry = require('web.field_registry');
    var ViewRegistry = require('web.view_registry');
    var relational_fields = require("web.relational_fields");
    var FieldOne2Many = require('web.relational_fields').FieldOne2Many;
    var CalendarView = require("web.CalendarView");
    var GraphView = require("web.GraphView");
    var PivotView = require("web.PivotView");

    var viewClass = {
        graph: GraphView,
        pivot: PivotView,
        calendar: CalendarView,
        };

   FieldOne2Many.include({
        _render: function () {
            if (this.renderer || !this.view) return this._super();
            var arch = this.view.arch;
            if (
                arch.tag === "graph" ||
                arch.tag === "pivot" ||
                arch.tag === "calendar"
            ) {
                var viewType = arch.tag;
                var view_params = _.extend(this.value, {
                    ids: this.value.res_ids,
                    modelName: this.value.model,
                    groupBy: [],
                });
                var view = new viewClass[viewType](this.view, view_params);
                var self = this;
                return view.getController(this).then(function (controller) {
                    self.renderer = controller.renderer;
                    self.$el.addClass(
                        "o_field_x2many o_field_x2many_" + viewType
                    );
                    controller.appendTo(self.$el);
                    return;
                });
            } else return this._super();
        },
    });
});

